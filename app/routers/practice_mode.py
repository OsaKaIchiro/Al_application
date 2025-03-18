from fastapi import APIRouter, Request, Form, Depends, Cookie
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from app.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.practice_mode import ContextPut
from app.cruds.practice_mode import put_context

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# practice_modeに移動したときpractice_mode.htmlが返される
@router.get('/practice_mode', response_class=HTMLResponse)
async def get_practice_mode(request: Request):
    return templates.TemplateResponse('practice_mode.html', {'request': request})

# 質問がクライント側と側から送信される
@router.post('/practice_mode', response_model=ContextPut)
async def practice(request: Request, context: str = Form(...), db: AsyncSession = Depends(get_db), username: str = Cookie(None)):
    if username is None:
        return RedirectResponse('/log_in_page', status_code=303)
    response = await put_context(db, username, context)
    return response

# AIのAPIを使って、contextを送って[はい]か[いいえ]で受け取る.
# それをデータベースに保存してほしい



