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
        "status": "online"
    }

@app.get("/api/errors")
def get_errors():
    return [
        {"timestamp": "2026-03-08 16:30:45", "message": "Connection timeout on guild sync"},
        {"timestamp": "2026-03-08 16:25:12", "message": "Database query exceeded timeout"},
        {"timestamp": "2026-03-08 16:15:33", "message": "Rate limit warning from Discord API"},
    ]

static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")
