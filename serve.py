## A simple FastAPI server that exposes a Langchain pipeline as an API endpoint.


from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_ollama import ChatOllama
from langserve import add_routes
import os


model = ChatOllama(model = "llama3.1")


system_template = "Translate the following into {language}"

prompt = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

parser = StrOutputParser()

## Create chain

chain = prompt|model|parser

## App definition

app = FastAPI(
    title = "Langchain server",
    version = 1.0,
    description = "a simple API server using Langchain runnable interfaces"
    )

add_routes(
    app ,
    chain,
    path = "/chain"
)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host = "localhost", post = 8000
    )