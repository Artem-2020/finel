from fastapi import FastAPI

app = FastAPI(title="FastAPI Hello")

@app.get("/")
async def hello():
    return {"message": "Hello, FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)