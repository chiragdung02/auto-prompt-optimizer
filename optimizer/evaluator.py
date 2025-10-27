import os
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def evaluate_prompt(prompt_text, input_text, ideal_output=None):
    """
    Evaluate a given prompt by sending it to OpenRouter.
    Returns: (response_text, tokens, score)
    """
    if not OPENROUTER_API_KEY:
        return "❌ Missing OPENROUTER_API_KEY. Set it using: setx OPENROUTER_API_KEY your_api_key_here", 0, 0

    combined_prompt = f"{prompt_text}\n\nUser Input:\n{input_text}"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful AI prompt evaluator."},
            {"role": "user", "content": combined_prompt}
        ]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        print("DEBUG STATUS:", response.status_code)
        print("DEBUG RESPONSE:", response.text)

        if response.status_code != 200:
            return f"❌ API Error: {response.text}", 0, 0

        json_data = response.json()
        text = json_data["choices"][0]["message"]["content"]
        tokens = json_data.get("usage", {}).get("total_tokens", 0)

        # Simple quality score (length-based)
        score = min(len(text) / 100, 1.0) * 100

        return text, tokens, round(score, 2)

    except Exception as e:
        return f"❌ Error calling API: {str(e)}", 0, 0
