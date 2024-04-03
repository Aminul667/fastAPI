from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
async def get_posts():
    return {"data": "This is the post"}

@app.post("/createposts")
async def create_posts(new_post: Post):
    print("payload", new_post.title)
    return {"data": "new post"}
