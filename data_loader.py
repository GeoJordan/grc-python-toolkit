import pandas as pd

def load_controls(path: str) -> pd.DataFrame:
    return pd.read_csv(
        path,
        engine="python",
        quotechar='"',
        skip_blank_lines=True
    )