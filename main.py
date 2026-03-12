from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os
import aiohttp

app = FastAPI()

# 🔗 봇 API 주소 (봇 레포 Railway 주소)
BOT_URL = "https://fortunate-emotion-production-e4f7.up.railway.app/api/bot-stats"

# -----------------------------
# BOT STATS
# -----------------------------

@app.get("/api/stats")
async def get_stats():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{BOT_URL}/api/bot-stats") as resp:

                if resp.status == 200:
                    return await resp.json()

    except Exception as e:
        print("Stats error:", e)

    return {
        "guilds": 0,
        "verified_users": 0,
        "warn_records": 0
    }


# -----------------------------
# ECONOMY STATS
# -----------------------------

@app.get("/api/economy/stats")
async def economy_stats():

    try:
        async with aiohttp.ClientSession() as session:

            async with session.get(f"{BOT_URL}/api/economy/stats") as resp:

                if resp.status == 200:
                    return await resp.json()

    except Exception as e:
        print("Economy stats error:", e)

    return {
        "total_money":0,
        "users":0,
        "avg_money":0
    }


# -----------------------------
# LEADERBOARD
# -----------------------------

@app.get("/api/economy/leaderboard")
async def leaderboard():

    try:
        async with aiohttp.ClientSession() as session:

            async with session.get(f"{BOT_URL}/api/economy/leaderboard") as resp:

                if resp.status == 200:
                    return await resp.json()

    except Exception as e:
        print("Leaderboard error:", e)

    return []


# -----------------------------
# GRAPH
# -----------------------------

@app.get("/api/economy/graph")
async def graph():

    try:
        async with aiohttp.ClientSession() as session:

            async with session.get(f"{BOT_URL}/api/economy/graph") as resp:

                if resp.status == 200:
                    return await resp.json()

    except Exception as e:
        print("Graph error:", e)

    return []


# -----------------------------
# ERRORS
# -----------------------------

@app.get("/api/errors")
async def errors():
    return []


# -----------------------------
# STATIC DASHBOARD
# -----------------------------

static_dir = os.path.join(os.path.dirname(__file__), "static")

app.mount(
    "/",
    StaticFiles(directory=static_dir, html=True),
    name="static"
        )
