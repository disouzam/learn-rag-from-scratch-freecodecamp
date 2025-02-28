import marimo

__generated_with = "0.11.11"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _():
    print("First marimo notebook")
    return


if __name__ == "__main__":
    app.run()
