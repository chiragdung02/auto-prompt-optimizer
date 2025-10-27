# AutoPrompt Optimizer (v2) — OpenAI only

AutoPrompt Optimizer evaluates multiple prompt variants for a given LLM task and ranks them by semantic quality, brevity, and token cost. This version is simplified to support OpenAI only and is ready to run locally or deploy to Streamlit Cloud.

## Quick start (local)

1. Clone or unzip the project.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate    # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file (or set environment variable):
   ```
   OPENAI_API_KEY=sk-your-key
   ```
5. Run:
   ```bash
   streamlit run app.py
   ```

## Files
- `app.py` — Streamlit UI and orchestration
- `optimizer/` — core modules: evaluator, metrics, utils
- `data/` — example prompts & test dataset
- `tests/` — small unit tests for metrics (no OpenAI calls)
- `.github/workflows/streamlit_deploy.yml` — example CI (placeholder)
- `.env.example` — example env file

## Notes
- This project calls the OpenAI API; you will be billed according to your usage.
- SentenceTransformers will download model weights on first run (requires internet).
