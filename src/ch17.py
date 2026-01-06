import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import time

    import marimo as mo

    return mo, time


@app.cell
def _(mo, time):
    @mo.cache
    def heavy_computation() -> int:
        time.sleep(3)
        return 1

    heavy_computation()
    return


@app.cell
def _(mo):
    run_button = mo.ui.run_button()
    run_button
    return (run_button,)


@app.cell
def _(mo, run_button):
    mo.stop(not run_button.value, mo.md("↑ボタンを押して実行を開始してください"))
    return


@app.cell
def _():
    for i in range(100):
        if i == 50:
            breakpoint()  # ここで停止
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
