import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    slider = mo.ui.slider(start=1, stop=120, label="あなたの年齢は？")
    slider
    return (slider,)


@app.cell
def _(mo, slider):
    mo.md(f"あなたの年齢は {slider.value} 歳です。")
    return


@app.cell
def _(mo):
    mo.md(
        f"今日の気分はどうですか？ {mo.ui.dropdown(['最高', '普通', 'ちょっと疲れ気味'])}"
    )
    return


@app.cell
def _(mo):
    mo.ui.text(label="あなたの趣味を教えてください。")
    return


@app.cell
def _(mo):
    mo.ui.checkbox(label="marimoを友達に勧めたいですか？")
    return


@app.cell
def _(mo):
    mo.ui.text_area(label="marimoの感想を教えてください。")
    return


@app.cell
def _(mo):
    data_file = mo.ui.file(
        filetypes=[".csv", ".txt", ".tsv"],
        multiple=False,
        label="データファイルをアップロードしてください",
    )
    data_file
    return (data_file,)


@app.cell
def _(data_file, mo):
    f = data_file.value

    if f:
        content = f"""
            ファイル名: {f[0].name}\n
            コンテンツ: {f[0].contents[:64]}
            """
    else:
        content = "ファイルが選択されていません。"
    mo.md(content)
    return


@app.cell
def _(mo):
    count_button = mo.ui.button(label="カウント", value=0, on_click=lambda x: x + 1)
    count_button
    return (count_button,)


@app.cell
def _(count_button):
    count_button.value
    return


@app.cell
def _(mo):
    d = mo.ui.date(label="有給の希望日を入力してください。")
    d
    return (d,)


@app.cell
def _(d):
    d.value
    return


app._unparsable_cell(
    r"""
    b    ui_dict = mo.ui.dictionary(
        {
            \"height\": mo.ui.number(start=30, stop=220, label=\"身長(cm)\"),
            \"weight\": mo.ui.number(start=3, stop=200, label=\"体重\"),
        }
    )
    ui_dict
    """,
    name="_",
)


@app.cell
def _(mo, ui_dict):
    res = ui_dict.value
    bmi = res["weight"] / ((res["height"] / 100) ** 2)
    mo.md(f"あなたのBMIは{bmi:.1f}です。")
    return


@app.cell
def _(mo):
    scores = mo.ui.array(
        [
            mo.ui.number(start=0, stop=100, label="国語の得点"),
            mo.ui.number(start=0, stop=100, label="数学の得点"),
            mo.ui.number(start=0, stop=100, label="英語の得点"),
        ]
    )
    scores
    return (scores,)


@app.cell
def _(mo, scores):
    total = sum(scores.value)
    average = total / len(scores.value)
    mo.md(
        f"""
        合計得点： {total} 点
        平均点： {average:.1f} 点
        """
    )
    return


@app.cell
def _(mo):
    form = (
        mo.md(
            """
        名前： {name}
        年齢： {age}
        """
        )
        .batch(name=mo.ui.text(label="名前"), age=mo.ui.number(1, 120, label="年齢"))
        .form()
    )
    form
    return (form,)


@app.cell
def _(form):
    form.value
    return


if __name__ == "__main__":
    app.run()
