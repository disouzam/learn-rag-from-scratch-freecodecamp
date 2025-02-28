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


@app.cell
def _():
    import os
    os.environ['LANGCHAIN_TRACING_V2'] = 'true'
    os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
    os.environ['LANGCHAIN_API_KEY'] = '<your-api-key>'
    os.environ['OPENAI_API_KEY'] = '<your-openai-api-key>'
    return (os,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Part 1: Overview

        RAG quickstart
        """
    )
    return


@app.cell
def _():
    import bs4
    from langchain import hub
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_community.document_loaders import WebBaseLoader
    from langchain_community.vectorstores import Chroma
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.runnables import RunnablePassthrough
    from langchain_openai import ChatOpenAI, OpenAIEmbeddings

    ### INDEXING

    # Load Documents
    loader = WebBaseLoader(
        web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
        bs_kwargs=dict(
            parse_only=bs4.SoupStrainer(
                class_=("post-content", "post-title", "post-header")
            )
        ),
    )
    docs = loader.load()

    # Split
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits=text_splitter.split_documents(docs)

    # Embed
    vectorstore = Chroma.from_documents(documents=splits,
                                       embedding=OpenAIEmbeddings(

                                       ))

    retriever = vectorstore.as_retriever()
    return (
        ChatOpenAI,
        Chroma,
        OpenAIEmbeddings,
        RecursiveCharacterTextSplitter,
        RunnablePassthrough,
        StrOutputParser,
        WebBaseLoader,
        bs4,
        docs,
        hub,
        loader,
        retriever,
        splits,
        text_splitter,
        vectorstore,
    )


if __name__ == "__main__":
    app.run()
