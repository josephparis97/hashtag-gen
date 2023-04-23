from hashtaggen import getHashtags
from fastapi import FastAPI, HTTPException
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

@app.get("/getHashtags")
async def get_hashtags_route(userInput: str):
    response = getHashtags(userInput)
    return {"hashtags": response}