from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {
        "message": "Hello World! Deployed through CI/CD"
    }

@app.get("/health")
def health():
    return {
        "message": "Checking health"
    }