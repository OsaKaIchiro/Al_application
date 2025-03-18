from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import app.models.table as models
import app.schemas.ranking as schemas

async def get_money_ranking(db: AsyncSession) -> list[schemas.MoneyRanking]:
    result = await db.execute(select(models.User).order_by(models.User.credits.desc()))
    users = result.scalars().all()
    
    ranking = []
    current_rank = 1
    previous_credits = None
    for i, user in enumerate(users):
        if previous_credits is not None and user.credits < previous_credits:
            current_rank = i + 1
        ranking.append(schemas.MoneyRanking(rank=current_rank, username=user.username, credits=user.credits))
        previous_credits = user.credits
    
    return ranking