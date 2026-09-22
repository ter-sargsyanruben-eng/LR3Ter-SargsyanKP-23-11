from pathlib import Path
import pandas as pd


def build_table(rows, output_csv="output/results.csv"):
    dataframe = pd.DataFrame(rows)
    Path(output_csv).parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(output_csv, index=False, encoding="utf-8-sig")
    return dataframe
