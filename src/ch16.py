import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import anywidget
    import marimo as mo
    import traitlets
    from drawdata import ScatterWidget

    return ScatterWidget, anywidget, mo, traitlets


@app.cell
def _(ScatterWidget, mo):
    widget = mo.ui.anywidget(ScatterWidget())
    widget
    return


@app.cell
def _(anywidget, mo, traitlets):
    class CounterWidget(anywidget.AnyWidget):
        # フロントエンドのロジック (JavaScript)
        _esm = """
        function render({ model, el }) {
          let button = document.createElement("button");
          button.innerHTML = `count is ${model.get("count")}`;
          button.onclick = () => {
            model.set("count", model.get("count") + 1);
            model.save_changes();
          };
          model.on("change:count", () => {
            button.innerHTML = `count is ${model.get("count")}`;
          });
          el.appendChild(button);
        }
        export default { render };
        """
        # Pythonと共有する変数
        count = traitlets.Int(0).tag(sync=True)

    # 独自のウィジェットを実行
    counter = mo.ui.anywidget(CounterWidget())
    counter
    return


if __name__ == "__main__":
    app.run()
