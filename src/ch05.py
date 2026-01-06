import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    x = 10
    return (x,)


@app.cell
def _(x):
    y = x + 5
    return (y,)


@app.cell
def _(y):
    print(y)
    return


@app.cell
def _():
    data = 1
    return


@app.cell
def _():
    # data = 2 # Error: This cell wasn't run because it has errors
    return


if __name__ == "__main__":
    app.run()
