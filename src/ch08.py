import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path

    import altair as alt
    import leafmap
    import marimo as mo
    import matplotlib.pyplot as plt
    import plotly
    import plotly.express as px
    import polars as pl
    import seaborn as sns

    this_dir = Path(__file__).parent
    data_path = this_dir / "data" / "scores.csv"
    return alt, data_path, leafmap, mo, pl, plt, px, sns


@app.cell
def _(data_path, pl):
    source_df = pl.read_csv(data_path).with_columns(
        total_score=pl.sum_horizontal(
            ["japanese", "math", "english", "science", "social"]
        )
    )
    return (source_df,)


@app.cell
def _(plt, sns, source_df):
    fig, ax = plt.subplots()
    sns.histplot(data=source_df, x="english", bins=10, ax=ax)
    ax
    return


@app.cell
def _(alt, mo, source_df):
    chart = alt.Chart(source_df).mark_point().encode(x="japanese", y="english")
    interactive_chart = mo.ui.altair_chart(chart)
    interactive_chart
    return


@app.cell
def _(mo, px, source_df):
    fig_px = px.scatter(
        source_df,
        x="math",
        y="science",
        size="total_score",
        color="gender",
        hover_name="name",
        title="Math vs Science (Size: Total Score)",
        color_discrete_sequence=px.colors.qualitative.Prism,
        template="plotly_white",
    )
    fig_px.update_layout(
        title_font_size=20,
        margin=dict(l=40, r=40, t=60, b=40),
    )
    interactive_plotly = mo.ui.plotly(fig_px)
    interactive_plotly
    return


@app.cell
def _(leafmap):
    m = leafmap.Map(center=[37.0, 138.0], zoom=5)
    m  # 日本地図が表示される
    return


if __name__ == "__main__":
    app.run()
