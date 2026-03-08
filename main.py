from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

@app.get("/api/stats")
def get_stats():
    return {
        "guilds": 42,
        "verified_users": 1250,
        "warn_records": 18,
    }

@app.get("/api/errors")
def get_errors():
    return []

static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")
