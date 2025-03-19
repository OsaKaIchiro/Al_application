from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from app.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.ranking import MoneyRanking
from app.cruds.ranking import get_money_ranking

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get('/ranking', response_class=HTMLResponse)
async def practice_ranking(request: Request, db: AsyncSession = Depends(get_db)):
    ranking = await get_money_ranking(db)
    return templates.TemplateResponse('ranking.html', {'request': request, 'ranking': ranking})

@router.get('/ranking2', response_class=HTMLResponse)
async def practice_ranking(request: Request, db: AsyncSession = Depends(get_db)):
    return templates.TemplateResponse('ranking2.html', {'request': request,})

@router.get('/ranking3', response_class=HTMLResponse)
async def practice_ranking(request: Request, db: AsyncSession = Depends(get_db)):
    return templates.TemplateResponse('ranking3.html', {'request': request})