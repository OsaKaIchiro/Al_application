from fastapi import APIRouter, Request, Form, Depends, Cookie
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from app.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.casual_mode import ContextPut
from app.cruds.casual_mode import put_context
from app.gemini import ask_gemini

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# practice_modeに移動したときpractice_mode.htmlが返される
@router.get('/casual_mode', response_class=HTMLResponse)
async def get_practice_mode(request: Request):
    return templates.TemplateResponse('casual_mode.html', {'request': request})

# 質問がクライント側と側から送信される
@router.post('/casual_mode', response_model=ContextPut)
async def practice(
    request: Request,
    context: str = Form(...),
    db: AsyncSession = Depends(get_db),
    username: str = Cookie(None)
):
    if username is None:
        return RedirectResponse('/log_in_page', status_code=303)

    # Geminiにcontextを渡して結果を取得
    gemini_response = await ask_gemini(context)

    # データベースに保存
    response = await put_context(db, username, gemini_response)
    return response

# AIのAPIを使って、contextを送って[はい]か[いいえ]で受け取る.
# それをデータベースに保存してほしい



