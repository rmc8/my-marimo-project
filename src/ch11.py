import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.image(src="https://marimo.io/logo.png", width=200, alt="marimo logo")
    return


@app.cell
def _(mo):
    mo.audio(src="public/shinshun.mp3")
    # フリー音源を利用しています => https://dova-s.jp/bgm/play23012.html
    return


@app.cell
def _(mo):
    mo.video(
        src="https://b.rmc-8.com/img/2025/12/09/dbefe05fd25968d582f203180977bdd1.mp4",
        width=480,
    )
    return


@app.cell
def _(mo):
    mo.pdf(src="public/paper.pdf", width="100%", height="500px")
    return


@app.cell
def _(mo):
    mo.md(
        f"""
        ### 実行結果の確認
    
        取得した画像はこちらです↓
        {mo.image(src="https://marimo.io/logo.png", width=300)}
        """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
