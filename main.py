from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel

app= FastAPI()
user_input_data = []

@app.get("/article")
def article():
    return FileResponse('article.html')

@app.get("/novel")
def novel():
    return FileResponse('novel.html')

@app.post("/save_conversation")
async def save_conversation(request: Request):
    conversation = await request.json()
    with open("conversations.txt", "a") as file:
        file.write(str(conversation) + "\n")
    return {"message": "Conversation saved successfully."}