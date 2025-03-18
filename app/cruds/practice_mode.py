from sqlalchemy.ext.asyncio import AsyncSession
import app.models.table as Practice_Mode
from sqlalchemy.future import select
import app.schemas.practice_mode as practice

async def put_context(db: AsyncSession, info_username: str, context: str) -> practice.ContextPut:
    new_context = Practice_Mode.Practice_context(username=info_username, context=context)
    db.add(new_context)
    await db.commit()
    await db.refresh(new_context)
    return new_context