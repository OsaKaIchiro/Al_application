from fastapi import APIRouter, Request, Form, Depends, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from app.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.log_in_page import UserResponse, LoginResponse, NewUserResponse
from app.cruds.log_in_page import create_user, sign_in
from app.cruds.home import get_money


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

#ルートディレクトリに入った時.htmlが返される
@router.get('/', response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse('a.html', {'request': request})

# ログインページに入った時log_in_page.htmlが返される
@router.get('/log_in_page', response_class=HTMLResponse)
async def get_log_in_page(request: Request):
    return templates.TemplateResponse('log_in_page.html', {'request': request})

# サインイン時
@router.post('/log_in_page', response_class=HTMLResponse)
async def post(request: Request, response: Response, info_username_1: str = Form(...), info_password_1: str = Form(...), db: AsyncSession = Depends(get_db)):
    response_data = await sign_in(db, info_username_1, info_password_1)
    if response_data.success:
        response.set_cookie(
            key="username",
            value=info_username_1,
            httponly=True,
            max_age=7200,  # 2時間
            secure=False,  # HTTPSを使用していない場合はFalse
            path="/"       # Cookieをすべてのパスで利用可能にする
        )
        credits_response = await get_money(db, info_username_1)
        return templates.TemplateResponse('home.html', {'request': request, 'username': info_username_1, 'credits': credits_response.credits})
    else:
        return templates.TemplateResponse('log_in_page.html', {'request': request, 'success': response_data.success})

# ログイン時に/newに移動する
@router.get('/new', response_class=HTMLResponse)
async def get_new(request: Request):
    return templates.TemplateResponse('new.html', {'request': request})

@router.post('/new', response_class=HTMLResponse)
async def post_new(request: Request, info_username_2: str = Form(...), info_password_2: str = Form(...), db: AsyncSession = Depends(get_db)):
    response = await create_user(db, info_username_2, info_password_2)
    if response.success1 and response.success2:
        return RedirectResponse('/log_in_page', status_code=303)
    else:
        return templates.TemplateResponse('new.html', {'request': request, 'success1': response.success1, 'success2': response.success2})