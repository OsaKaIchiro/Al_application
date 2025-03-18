from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import log_in_page, ranking, home, casual_mode


app = FastAPI()
app.mount("/static" , app=StaticFiles(directory = "/app"), name = "static")
app.include_router(log_in_page.router)
app.include_router(ranking.router)
app.include_router(casual_mode.router)
