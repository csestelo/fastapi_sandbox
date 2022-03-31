from fastapi import FastAPI


app = FastAPI()


@app.get("/")
@app.get("/health_check")
async def ping():
    return {"message": "PONG! App running!"}
