from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from app.db import get_db
from app.models.table import User, Practice_context
import random
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.casual_mode import ContextPut
from app.cruds.casual_mode import put_context
from app.gemini import ask_gemini
from sqlalchemy.orm import sessionmaker
import asyncio
from fastapi import Depends

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


async def get_contents_list(session: AsyncSession):
    count_all = await session.scalar(select(func.count()).select_from(select(Practice_context).subquery()))
    if count_all >= 10:
        data_list = random.sample(range(1, count_all + 1), 10)
        contents_list = []
        for i in data_list:
            no_name = await session.get(Practice_context, i)
            if no_name:
                contents_list.append(no_name.context)
        return contents_list
    elif count_all == 0:
        return []
    else:
        contents_list = []
        for i in range(1, count_all + 1):
            no_name = await session.get(Practice_context, i)
            if no_name:
                contents_list.append(no_name.context)
        return contents_list

@router.get('/casual_mode', response_class=HTMLResponse)
async def get(request: Request, session: AsyncSession = Depends(get_db)):
    contents_list = await get_contents_list(session)
    return templates.TemplateResponse(
        'casual_mode.html',
        {
            'request': request,
            'contents_list': contents_list
        }
    )

@router.post('/casual_mode', response_class=HTMLResponse)
async def post(request: Request, idea_data: str = Form(...), session: AsyncSession = Depends(get_db)):
    practice_context = Practice_context(username = 'qqq', context=idea_data) #usernameは適宜変更してください。
    session.add(practice_context)
    await session.commit()
    contents_list = await get_contents_list(session)
    return templates.TemplateResponse(
        'casual_mode.html',
        {
            'request': request,
            'contents_list': contents_list
        }
    )

@router.get('/home', response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse(
        'home.html',
        {
            'request': request
        }
    )





