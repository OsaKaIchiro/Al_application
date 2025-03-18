from sqlalchemy.ext.asyncio import AsyncSession
import app.models.table as catch_money_model
from sqlalchemy.future import select
import app.schemas.home as home_get_money

async def get_money( db: AsyncSession, const_username: str) -> home_get_money.GetMoney:
    #resposeに
    result = await db.execute(select(catch_money_model.User).filter(catch_money_model.User.username == const_username))
    user = result.scalars().first()

    if user :
        return home_get_money.GetMoney(username=user.username, credits=user.credits)