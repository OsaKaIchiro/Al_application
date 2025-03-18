from sqlalchemy.ext.asyncio import AsyncSession
import app.models.table as casual_mode_model
from sqlalchemy.future import select
<<<<<<< HEAD
import app.schemas.casual_mode as practice

async def put_context(db: AsyncSession, info_username: str, context: str) -> practice.ContextPut:
    new_context = Practice_Mode.Practice_context(username=info_username, context=context)
    db.add(new_context)
    await db.commit()
    await db.refresh(new_context)
    return new_context
=======
import app.schemas.casual_mode as casual_mode_schema
>>>>>>> 47ae6ee877176a1e6a101269ce74cab9b1be038e
