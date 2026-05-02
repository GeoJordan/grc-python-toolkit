import os

def export_csv(df, path):
    directory = os.path.dirname(path)

    if directory:
        os.makedirs(directory, exist_ok=True)

    df.to_csv(path, index=False)