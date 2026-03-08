from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

@app.get("/api/stats")
def get_stats():
    return {
        "servers": 42,
        "users": 1250,
        "warnings": 18,
        "status": "online"
    }

static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")
