# 🚀 Auto Prompt Optimizer

**Auto Prompt Optimizer** is an intelligent Python-based tool that automatically enhances, refines, and evaluates AI prompts using OpenRouter’s cutting-edge LLM APIs.  
It helps developers, AI researchers, and creators improve prompt effectiveness for tasks like writing, coding, analysis, or generation — all with a single click.

---

## 🌟 Features

- 🧠 **Automated Prompt Improvement** – Uses LLM models to rewrite and optimize prompts.
- ⚙️ **Scoring System** – Rates prompts based on clarity, specificity, and effectiveness.
- 🔁 **Multiple Iterations** – Generates improved versions until the best output is found.
- 🧩 **Customizable Configs** – Change API keys, models, or settings easily in `.env`.
- 🪶 **Lightweight UI (Optional)** – Launch with a single `run_project.bat` file.
- 🛠️ **Fully Open Source** – Build, extend, and deploy your own version.

---

## 🧩 Tech Stack

- **Language:** Python 3.10+
- **API Provider:** [OpenRouter API](https://openrouter.ai)
- **Libraries Used:**  
  - `requests`  
  - `dotenv`  
  - `argparse`  
  - `json`  
  - `time`

---

## 🏗️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/chiragdung02/auto-prompt-optimizer.git
cd auto-prompt-optimizer
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On Mac/Linux
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment
Rename `.env.example` to `.env` and fill in your OpenRouter API key:
```
OPENROUTER_API_KEY=your_api_key_here
```

Get your free API key here → [https://openrouter.ai/keys](https://openrouter.ai/keys)

---

## ▶️ Running the Project

### Option 1: Run with Python
```bash
python app.py
```

### Option 2: Run via Batch File (Windows)
Double-click on:
```
run_project.bat
```

---

## 📊 Example Workflow

1. Input a raw prompt (e.g., *“Write a story about space”*)  
2. The system sends it to the OpenRouter LLM API.  
3. It evaluates, improves, and ranks better versions.  
4. The final optimized prompt is displayed and saved.  

---

## 💻 Demo Preview

![Auto Prompt Optimizer UI Preview](A_screenshot_of_an_application_named_"Auto_Prompt_.png)

*(Soft pulsing overlay aesthetic used for modern visual demo.)*

---

## 📁 Folder Structure
```
auto-prompt-optimizer/
│
├── data/                 # Stores logs & prompt results
├── optimizer/            # Core optimization logic
├── tests/                # Unit tests
├── .env.example          # Environment variable example
├── LICENSE               # Open source license
├── README.md             # This file
├── app.py                # Main entry script
├── requirements.txt      # Dependencies
└── run_project.bat       # Windows launch script
```

---

## 🧠 Future Enhancements

- [ ] Add web UI using Streamlit  
- [ ] Integrate Hugging Face hub deployment  
- [ ] Support multiple models in rotation  
- [ ] Add prompt analytics dashboard  

---

## 👤 Author

**Chirag Dung**  
🔗 [GitHub Profile](https://github.com/chiragdung02)

---

## 🪪 License

This project is licensed under the **MIT License** — free to use, modify, and distribute with attribution.

---

## ⭐ Support

If you like this project, give it a star 🌟 on [GitHub](https://github.com/chiragdung02/auto-prompt-optimizer)  
and share your feedback or ideas in the Issues tab!
