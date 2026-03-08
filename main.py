from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# static 폴더 경로 확인
static_dir = os.path.join(os.path.dirname(__file__), "static")

app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")
