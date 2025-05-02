from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"message": "pong"}

@app.get("/comida")
async def proway():
    return {"message": "carne"}