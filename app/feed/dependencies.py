from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.feed.crud import FeedCRUD


async def get_feed_crud(
        session: AsyncSession = Depends(get_async_session)
) -> FeedCRUD:
    return FeedCRUD(session=session)
