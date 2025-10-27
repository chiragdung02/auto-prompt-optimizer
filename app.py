import streamlit as st
from optimizer.evaluator import evaluate_prompt

# --- App Config ---
st.set_page_config(page_title="Auto Prompt Optimizer (OpenRouter version)", page_icon="🚀", layout="wide")

# --- Title Section ---
st.markdown("""
# 🚀 Auto Prompt Optimizer (OpenRouter version)

This app helps you analyze, test, and score prompts automatically using the OpenRouter API.  
""")

# --- Example Prompts Dictionary ---
examples = {
    "🧠 Summarization": {
        "prompt": "Summarize the following text in one short, clear paragraph, keeping only the main ideas and removing unnecessary details.",
        "input": """Artificial Intelligence (AI) is rapidly transforming every industry, from healthcare to finance. In hospitals, AI helps doctors diagnose diseases earlier, while in banking, algorithms detect fraud faster than humans. However, experts warn that without proper regulation, AI could also cause job losses and raise ethical challenges about privacy and fairness.""",
        "ideal": "AI is revolutionizing industries like healthcare and finance by improving efficiency and accuracy, but it also raises concerns about ethics, privacy, and job loss."
    },
    "✨ Product Description": {
        "prompt": "Write a catchy 2-line product description that appeals to Gen-Z buyers.",
        "input": "Pastel pink sneakers made from recycled ocean plastic.",
        "ideal": "Step soft, tread bold 🌊💗 — made from ocean love and Gen-Z flair. Pastel kicks that make every step guilt-free and iconic."
    },
    "💬 Customer Support": {
        "prompt": "You are a polite and empathetic AI assistant. Respond kindly and helpfully to the user’s complaint.",
        "input": "My sandals broke after just 3 days of wearing them. This is really disappointing!",
        "ideal": "I’m so sorry to hear that your sandals broke! That’s not the experience we want for our customers. Please share your order number and we’ll send you a replacement right away."
    }
}

# --- Example Loader UI ---
st.sidebar.header("💡 Load Example Prompt")
example_choice = st.sidebar.selectbox("Select an example:", ["None"] + list(examples.keys()))

if example_choice != "None":
    st.session_state["prompt_text"] = examples[example_choice]["prompt"]
    st.session_state["input_text"] = examples[example_choice]["input"]
    st.session_state["ideal_output"] = examples[example_choice]["ideal"]
    st.sidebar.success(f"✅ Loaded example: {example_choice}")

# --- Input Fields ---
st.subheader("✍️ Enter your Prompt Template")
prompt_text = st.text_area(
    "Prompt Template",
    st.session_state.get("prompt_text", ""),
    height=120,
    placeholder="e.g., Summarize any text in one paragraph..."
)

st.subheader("🧾 Sample Input")
input_text = st.text_area(
    "Sample Input",
    st.session_state.get("input_text", ""),
    height=120,
    placeholder="Paste a sample user input here..."
)

st.subheader("🌟 Ideal Output (optional)")
ideal_output = st.text_area(
    "Ideal Output (optional)",
    st.session_state.get("ideal_output", ""),
    height=100,
    placeholder="What a perfect response might look like..."
)

# --- Evaluate Button ---
if st.button("🔍 Evaluate Prompt", use_container_width=True):
    if not prompt_text.strip() or not input_text.strip():
        st.error("⚠️ Please fill in both the prompt template and sample input.")
    else:
        with st.spinner("Evaluating prompt... ⏳"):
            try:
                output_text, tokens, score = evaluate_prompt(prompt_text, input_text)
                st.success("✅ Evaluation complete!")

                st.markdown("### 🧠 Model Output")
                st.write(output_text)

                st.markdown("### 📊 Evaluation Summary")
                st.write(f"**Total Tokens Used:** {tokens}")
                st.write(f"**Prompt Score:** {score}/100")

            except Exception as e:
                st.error(f"Error during evaluation: {e}")

# --- Footer ---
st.markdown("---")
st.caption("Built with ❤️ using OpenRouter & Streamlit — Auto Prompt Optimizer v2 by Chirag Dung.")
