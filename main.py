from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
async def get_posts():
    return {"data": "This is the post"}

@app.post("/createposts")
async def create_posts(payload: dict=Body(...)):
    print("Hi This is payload", payload)
    return {"rew_post": f"title is {payload['title']} and the content is {payload['content']}"}
