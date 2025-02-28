import marimo

__generated_with = "0.11.11"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        (1) Packages

        - pip install langchain_community
        - pip install tiktoken
        - pip install langchain-openai
        - pip install langchainhub
        - pip install chromadb
        - pip install langchain
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        (2) LangSmith

        [https://docs.smith.langchain.com/](https://docs.smith.langchain.com/)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Part 1: Overview

        RAG quickstart
        """
    )
    return


if __name__ == "__main__":
    app.run()
