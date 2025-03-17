from fastapi import APIRouter , Request , Form  , Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from app.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.log_in_page import UserResponse, LoginResponse, NewUserResponse
from app.cruds.home import get_money

router = APIRouter()
templates = Jinja2Templates(directory = "app/templates")

#お金の取得
@router.get('/home', response_class=HTMLResponse)
async def get_home(request: Request, db: AsyncSession = Depends(get_db)):
    response = await get_money(db)
    return templates.Templateresponse('home.html', {'request': request, 'money': response.money})

