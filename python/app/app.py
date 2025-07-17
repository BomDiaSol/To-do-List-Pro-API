from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def get_root():
    return "v0.0"

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)