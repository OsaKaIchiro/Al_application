from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import log_in_page


app = FastAPI()
<<<<<<< HEAD
app.mount("/static" , app=StaticFiles(directory = "/app"), name = "static")
=======
app.mount(path="/static" , app=StaticFiles(directory = "/app"), name = "static")
>>>>>>> photo_add
app.include_router(log_in_page.router)

