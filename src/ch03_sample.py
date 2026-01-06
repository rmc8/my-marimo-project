import marimo

__generated_with = "0.18.4"
app = marimo.App()


@app.cell
def _():
    import polars as pl

    df = pl.DataFrame(
        {
            "height": [160.1, 155.7, 172.9, 149.3, 183.1],
            "weight": [55.3, 51.2, 66.9, 49.2, 70.1],
        },
    )
    df.head()
    return


if __name__ == "__main__":
    app.run()
