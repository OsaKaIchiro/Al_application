from sqlalchemy.ext.asyncio import AsyncSession
<<<<<<< HEAD
import app.models.table as sign_in_page_model
=======
import Al_application.app.models.table as sign_in_page_model
>>>>>>> photo_add
from sqlalchemy.future import select
import app.schemas.log_in_page as sign_in_page_schema


#新規登録の情報をデータベースに保存/成否を返す関数
async def create_user(
    db: AsyncSession, info_username_2: str, info_password_2: str
) -> sign_in_page_schema.NewUserResponse:
    success1 = True
    success2 = True
    error = False

    #データベースに接続してuser_allにテーブルを格納
    result = await db.execute(select(sign_in_page_model.User))
    user_all = result.scalars().all()

    for i in user_all:
        if i.username == info_username_2:
            success1 = False
            error = False
    if not info_password_2.isalnum():
        success2 = False
        error = True
    if len(info_password_2) < 8:
        success2 = False
        error = True

    
    if error:
        return sign_in_page_schema.NewUserResponse(success1=success1, success2=success2)
    else:
        user = sign_in_page_model.User()
        user.username = info_username_2
        user.password = info_password_2
        user.credits = 1000 #初期値を1000円にします
        db.add(user)
        await db.commit()
        return sign_in_page_schema.NewUserResponse(success1=success1, success2=success2)



#ログインするときusernameとpasswordがあっているかどうかを確認する
async def sign_in(db: AsyncSession, info_username_1: str, info_password_1: str) -> sign_in_page_schema.LoginResponse:
    success = False

    result = await db.execute(select(sign_in_page_model.User))
    user_all = result.scalars().all()

    for i in user_all:
        if i.username == info_username_1 and i.password == info_password_1:
            success = True
            break
    if success:
        return sign_in_page_schema.LoginResponse(success=True, username=info_username_1)
    else:
        return sign_in_page_schema.LoginResponse(success=False)