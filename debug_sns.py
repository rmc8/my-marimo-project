from pathlib import Path

import matplotlib.pyplot as plt
import polars as pl
import seaborn as sns

this_dir = Path(__file__).parent
data_path = this_dir / "src" / "data" / "scores.csv"

try:
    df = pl.read_csv(data_path)
    print(f"Columns: {df.columns}")
    fig, ax = plt.subplots()
    sns.histplot(data=df, x="math", ax=ax)
    print("Success with data keyword")
    sns.histplot(df, x="math", ax=ax)
    print("Success with positional data")
except Exception as e:
    print(f"Error: {e}")
    import traceback

    traceback.print_exc()
