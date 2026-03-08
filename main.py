from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os
import aiohttp

app = FastAPI()

# ✅ Bot의 실제 공개 도메인
BOT_API_URL = "https://fortunate-emotion-production-e4f7.up.railway.app/api/bot-stats"

@app.get("/api/stats")
async def get_stats():
    try:
        print(f"Calling bot API: {BOT_API_URL}")
        async with aiohttp.ClientSession() as session:
            async with session.get(
                BOT_API_URL, 
                timeout=aiohttp.ClientTimeout(total=10),
                ssl=False
            ) as resp:
                print(f"Bot API response: {resp.status}")
                if resp.status == 200:
                    data = await resp.json()
                    print(f"Got bot data: {data}")
                    return data
                else:
                    print(f"Bot API error: {resp.status}")
    except Exception as e:
        print(f"Exception: {e}")
    
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
