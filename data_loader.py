import pandas as pd

def load_controls(file):
    try:
        return pd.read_csv(file)
    except Exception:
        file.seek(0)
        return pd.read_csv(
            file,
            engine="python",
            quotechar='"',
            skip_blank_lines=True
        )