from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {
        "message":"Hello from ci-cd demo"
    }

@app.get("/health")
def health():
    return {
        "status":"healthy"
    }