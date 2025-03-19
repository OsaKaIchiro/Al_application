from sqlalchemy.ext.asyncio import AsyncSession
import app.models.table as casual_mode_model
from sqlalchemy.future import select
import app.schemas.casual_mode as casual_mode_schema
import random
from app.models.table import User, Practice_context
from sqlalchemy import select, func


async def put_context(db: AsyncSession, info_username: str, context: str) -> casual_mode_schema.ContextPut:
    new_context = casual_mode_model.Practice_context(username=info_username, context=context)
    db.add(new_context)
    await db.commit()
    await db.refresh(new_context)
    return casual_mode_schema.ContextPut(username=new_context.username, context=new_context.context)


async def get_contents_list(session: AsyncSession):
    # Practice_contextテーブルからすべてのデータを取得
    result = await session.execute(select(Practice_context.context))
    all_contexts = [row[0] for row in result.fetchall()]

    # データが10件以上の場合はランダムに10件選択、それ以外はすべて返す
    if len(all_contexts) >= 10:
        return random.sample(all_contexts, 10)
    return all_contexts
