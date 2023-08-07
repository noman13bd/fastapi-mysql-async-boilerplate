from fastapi import APIRouter, Depends
from fastapi import status as http_status
from app.feed.crud import FeedCRUD
from app.feed.dependencies import get_feed_crud

router = APIRouter()

@router.get(
    "",
    status_code=http_status.HTTP_200_OK
)
async def get_mysql_data(feedCrud: FeedCRUD = Depends(get_feed_crud)):
    return await feedCrud.get()