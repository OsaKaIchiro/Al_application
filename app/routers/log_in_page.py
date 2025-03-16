from fastapi import APIRouter , Request , Form  
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from app.db import session
from app.models.log_in_page import User

router = APIRouter()
router.mount("/static" , StaticFiles(directory = "app/static"), name = "static")
templates = Jinja2Templates(directory = "app/templates")

@router.get('/' , response_class=HTMLResponse)
async def get(request:Request):
    return templates.TemplateResponse(
        'log_in_page.html',
        {
            'request' : request
        }
    )


@router.post('/' , response_class=HTMLResponse)
async def post(request:Request , info_username_1 : str = Form(...) , info_password_1 : str = Form(...)):
    success = 0

    user_all = session.query(User).all()
    for i in user_all:
        if i.username == info_username_1 and i.password == info_password_1:
            success = 1
    if success:
        return templates.TemplateResponse(
            'content.html',
            {
                'request' : request,
                'username':info_username_1
            }
        )
    else:
        return templates.TemplateResponse(
            'login_in_page.html',
            {
                'request':request,
                'success':success
            }
        )

@router.get('/new' , response_class=HTMLResponse)
async def get(request:Request):
    return templates.TemplateResponse(
        'new.html',
        {
            'request' : request
        }
    )

@router.post('/new' , response_class=HTMLResponse)
async def post(request:Request , info_username_2 : str = Form(...) , info_password_2 : str = Form(...)):
    success1 = 1
    success2 = 1
    error = 0
    user_all = session.query(User).all()
    for i in user_all:
        if i.username == info_username_2:
            success1 = 0
            error = 1
    if not info_password_2.isalnum():
        success2 = 0
        error = 1
    if len(info_password_2) < 8:
        success2 = 0
        error = 1

    if error:
        return templates.TemplateResponse(
            'new.html',
            {
                'request' : request,
                'success1' :success1,
                'success2':success2
            }
        )
    else:
        user = User()
        user.username = info_username_2
        user.password = info_password_2
        session.add(user)
        session.commit()
        return RedirectResponse('/' , status_code=301)