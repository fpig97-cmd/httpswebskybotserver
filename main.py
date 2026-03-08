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
async def get_errors():
    """Bot에서 에러 로그 가져오기"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://fortunate-emotion-production-e4f7.up.railway.app/api/errors",
                timeout=aiohttp.ClientTimeout(total=5),
                ssl=False
            ) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    print(f"Got {len(data)} error logs")
                    return data
    except Exception as e:
        print(f"Error logs API error: {e}")
    
    return []

static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")

