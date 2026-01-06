import marimo

__generated_with = "0.18.4"
app = marimo.App(app_title="Chap04")


@app.cell
def _():
    import marimo as mo
    import polars as pl
    return (pl,)


@app.cell
def _(pl):
    df = pl.DataFrame(
        {
            "height": [160.1, 155.7, 172.9, 149.3, 183.1],
            "weight": [55.3, 51.2, 66.9, 49.2, 70.1],
        },
    )
    df.head()
    return (df,)


@app.cell
def _(df, pl):
    df_bmi = df.with_columns(
        (
            pl.col("weight") / ((pl.col("height") / 100) ** 2)
        ).round(1).alias("BMI")
    )
    df_bmi.head()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
