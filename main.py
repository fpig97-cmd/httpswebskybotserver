from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os
import aiohttp

app = FastAPI()

@app.get("/api/stats")
async def get_stats():
    try:
        # Discord Bot API 호출 (8001 포트)
        async with aiohttp.ClientSession() as session:
            async with session.get("http://localhost:8001/api/bot-stats", timeout=aiohttp.ClientTimeout(total=5)) as resp:
                if resp.status == 200:
                    return await resp.json()
    except Exception as e:
        print(f"Bot API error: {e}")
    
    # Bot이 안 떠있으면 임시값 반환
    return {
        "guilds": 0,
        "verified_users": 0,
        "warn_records": 0,
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
