from fastapi import APIRouter, Depends
from fastapi import status as http_status
from app.core.celery_conf import celery_app
from app.feed.crud import FeedCRUD
from app.feed.dependencies import get_feed_crud

router = APIRouter()

@router.get(
    "",
    status_code=http_status.HTTP_200_OK
)
async def get_mysql_data(feedCrud: FeedCRUD = Depends(get_feed_crud)):
    custom_task.delay()
    custom_task2.delay()
    return await feedCrud.get()

@celery_app.task()
def custom_task():
    print("Hello from celery")
    return True

@celery_app.task()
def custom_task2():
    print("Hello from celery2")
