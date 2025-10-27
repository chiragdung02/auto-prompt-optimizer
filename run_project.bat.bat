@echo off
echo 🚀 Launching Auto Prompt Optimizer...

REM Step 1: Navigate to project folder
cd /d "C:\Users\chira\OneDrive\Desktop\auto-prompt-optimizer-v2"

REM Step 2: Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Step 3: Activate virtual environment
call venv\Scripts\activate

REM Step 4: Install dependencies if needed
echo Installing dependencies...
pip install -r requirements.txt

REM Step 5: Run Streamlit app
echo Starting Streamlit app...
streamlit run app.py

pause
