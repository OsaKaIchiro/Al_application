from fastapi import APIRouter , Request , Form  , Depends 
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from app.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.log_in_page import UserResponse, LoginResponse, NewUserResponse
from app.cruds.log_in_page import create_user, sign_in


router = APIRouter()
templates = Jinja2Templates(directory = "app/templates")

#ルートディレクトリに入った時log_onA_page.htmlが返される
@router.get('/', response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse('log_in_page.html', {'request': request})

#サインイン時
@router.post('/', response_model=LoginResponse)
async def post(request: Request, info_username_1: str = Form(...), info_password_1: str = Form(...), db: AsyncSession = Depends(get_db)):
    response = await sign_in(db, info_username_1, info_password_1)
    if response.success:
        return templates.TemplateResponse('context.html',{'request' : request})
    else:
        return templates.TemplateResponse('log_in_page.html', {'request': request, 'success': response.success})

#ログイン時に/newに移動する
@router.get('/new' , response_class=HTMLResponse)
async def get_new(request:Request):
    return templates.TemplateResponse('new.html',{'request' : request})


@router.post('/new', response_model=NewUserResponse)
async def post_new(request: Request, info_username_2: str = Form(...), info_password_2: str = Form(...), db: AsyncSession = Depends(get_db)):
    response = await create_user(db, info_username_2, info_password_2)
    if response.success1 and response.success2:
        return RedirectResponse('/', status_code=303)
    else:
        return templates.TemplateResponse('new.html', {'request': request, 'success1': response.success1, 'success2': response.success2})