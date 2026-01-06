import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path

    import marimo as mo
    import polars as pl

    this_dir = Path(__file__).parent
    data_path = this_dir / "data" / "data.csv"
    return data_path, mo, pl


@app.cell
def _(pl):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    df
    return


@app.cell
def _(data_path, mo, pl):
    source_df = pl.read_csv(data_path)
    transformed_df = mo.ui.dataframe(source_df)
    transformed_df
    return (source_df,)


@app.cell
def _(mo, source_df):
    fil_df = mo.sql(
        """
        SELECT
            height,
            weight
        FROM
            source_df
        WHERE
        	height >= 155
        	AND weight >=55
        """
    )
    return (fil_df,)


@app.cell
def _(fil_df):
    fil_df
    return


@app.cell
def _(fil_df):
    type(fil_df)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
