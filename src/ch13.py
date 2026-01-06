import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    print("ノートブックをpythonで実行するとそのままコンソールに出力されます。")
    return (mo,)


@app.cell
def _(mo):
    name = mo.cli_args().get("name", "Guest")
    mo.md(f"こんにちは、{name}さん！")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
