from sqlalchemy.ext.asyncio import AsyncSession
import app.models.table as casual_mode_model
from sqlalchemy.future import select
import app.schemas.casual_mode as practice

async def put_context(db: AsyncSession, info_username: str, context: str) -> practice.ContextPut:
    new_context = practice.Practice_context(username=info_username, context=context)
    db.add(new_context)
    await db.commit()
    await db.refresh(new_context)
    return new_context
