import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    get_count, set_count = mo.state(0)
    return get_count, set_count


@app.cell
def _(get_count, mo):
    mo.md(f"現在のカウント: {get_count()}")
    return


@app.cell
def _(set_count):
    # 直接更新
    set_count(10)
    return


@app.cell
def _(set_count):
    # 現在の値に基づいて更新
    set_count(lambda current: current + 1)
    return


@app.cell
def _(mo, set_count):
    # ボタンが押されるたびに set_count が実行される
    increment_btn = mo.ui.button(
        label="+1", on_change=lambda _: set_count(lambda n: n + 1)
    )
    increment_btn
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
