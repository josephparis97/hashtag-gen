from hashtaggen import getHashtags
from fastapi import FastAPI, HTTPException
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
handler = Mangum(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/getHashtags")
async def get_hashtags_route(userInput: str):
    response = getHashtags(userInput)
    return {"hashtags": response}