import pandas as pd

def load_prompts_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    if 'prompt' not in df.columns:
        raise ValueError("Prompts CSV must contain a 'prompt' column")
    return df

def load_test_dataset_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    expected_cols = {'input', 'expected_output'}
    if not expected_cols.issubset(set(df.columns)):
        raise ValueError("Test dataset CSV must contain 'input' and 'expected_output' columns")
    return df
