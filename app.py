from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)


add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

model=ChatOpenAI()
prompt=ChatPromptTemplate.from_template("provide me an essay about {topic}")
prompt1=ChatPromptTemplate.from_template("provide me a poem about {topic}")

add_routes(
    app,
    prompt|model,
    path="/essay"

)

add_routes(
    app,
    prompt1|model,
    path="/poem"

)

story_prompt = ChatPromptTemplate.from_template("write a short story about {topic}")
add_routes(
    app,
    story_prompt | model,
    path="/story"
)

dialogue_prompt = ChatPromptTemplate.from_template("write a conversation between {character1} and {character2} discussing {topic}")
add_routes(
    app,
    dialogue_prompt | model,
    path="/dialogue"
)

article_prompt = ChatPromptTemplate.from_template("write an article about {topic}")
add_routes(
    app,
    article_prompt | model,
    path="/article"
)



if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)