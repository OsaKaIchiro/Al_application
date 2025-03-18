from fastapi import APIRouter, Request, Form, Depends, Cookie
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from app.db import get_db
from app.models.table import User, Practice_context
import random
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.casual_mode import ContextPut
from app.cruds.casual_mode import put_context
from sqlalchemy.orm import sessionmaker
import asyncio
from app.cruds.casual_mode import put_context, get_contents_list
from fastapi import Depends

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get('/casual_mode', response_class=HTMLResponse)
async def get(request: Request, db: AsyncSession = Depends(get_db)):
    contents_list = await get_contents_list(db)
    return templates.TemplateResponse(
        'casual_mode.html',
        {
            'request': request,
            'contents_list': contents_list
        }
    )

#投稿された内容を表示
@router.post('/casual_mode', response_class=HTMLResponse)
async def post(request: Request, idea_data: str = Form(...), db: AsyncSession = Depends(get_db), username: str = Form(...)):
    print(f"Username from Cookie: {username}") 

    contents_list = await get_contents_list(db)
 # データベースでユーザー名を確認
    user_exists = await db.scalar(select(func.count()).select_from(User).where(User.username == username))
    if not user_exists:
        # ユーザー名が存在しない場合、エラーメッセージを表示
        return templates.TemplateResponse(
            'casual_mode.html',
            {
                'request': request,
                'miss': 'ユーザー名が間違っています',
                'contents_list': contents_list
            }
        )

    # データベースに保存
    await db.execute(
        Practice_context.__table__.insert().values(username=username, context=idea_data)
    )
    await db.commit()

    # コンテンツリストを取得してテンプレートに渡す
    contents_list = await get_contents_list(db)
    return templates.TemplateResponse(
        'casual_mode.html',
        {'request': request, 'contents_list': contents_list}
    )

@router.get('/home', response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse(
        'home.html',
        {
            'request': request
        }
    )





