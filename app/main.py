from fastapi import FastAPI

from app.routers import log_in_page


app = FastAPI()
app.include_router(log_in_page.router)

