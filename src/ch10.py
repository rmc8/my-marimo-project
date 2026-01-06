import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md("# タイトル"),
            mo.ui.slider(1, 10, label="スライダー"),
            mo.md("スライダーを操作できます。"),
        ]
    )
    return


@app.cell
def _(mo):
    mo.hstack(
        [
            mo.ui.button(label="保存"),
            mo.ui.button(label="削除"),
            mo.ui.button(label="キャンセル"),
        ],
        justify="start",
    )  # 左寄せ
    return


@app.cell
def _(mo):
    mo.ui.tabs(
        {
            "タブ1": mo.md("これはタブ1の内容です。"),
            "タブ2": mo.md("これはタブ2の内容です。"),
            "タブ3": mo.md("これはタブ3の内容です。"),
        }
    )
    return


@app.cell
def _(mo):
    mo.accordion(
        {
            "セクション1": mo.md("セクション1の内容です。"),
            "セクション2": mo.md("セクション2の内容です。"),
            "セクション3": mo.md("セクション3の内容です。"),
        }
    )
    return


@app.cell
def _(mo):
    mo.sidebar(
        mo.vstack(
            [
                mo.md("## サイドバー"),
                mo.ui.checkbox(label="オプション1"),
                mo.ui.checkbox(label="オプション2"),
                mo.ui.checkbox(label="オプション3"),
            ]
        )
    )
    return


@app.cell
def _(mo):
    height = 166.8
    weight = 65.2
    bmi = weight / (height / 100) ** 2
    mo.hstack(
        [
            mo.stat(
                value=height,
                label="身長",
                caption="+1.1cm(前年比)",
                direction="increase",
            ),
            mo.stat(
                value=weight,
                label="体重",
                caption="-0.5kg(前年比)",
                direction="decrease",
            ),
            mo.stat(
                value=bmi,
                label="BMI",
                caption="-0.49(前年比)",
                direction="decrease",
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md("""
    /// details | ソースコードを表示
    ```python
    def greet(name):
        return f"Hello, {name}!"

    print(greet("K"))
    ```
    ///
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    /// attention | 注意
    この操作は取り消せません！
    ///
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
