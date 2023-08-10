from fastapi import APIRouter, Depends
from fastapi import status as http_status
from app.core.celery_conf import celery_app
from elasticsearch import AsyncElasticsearch
from app.feed.crud import FeedCRUD
from app.feed.dependencies import get_feed_crud
from app import settings

router = APIRouter()

@router.get(
    "",
    status_code=http_status.HTTP_200_OK
)
async def get_mysql_data(feedCrud: FeedCRUD = Depends(get_feed_crud)):
    custom_task.delay()
    custom_task2.delay()
    es = AsyncElasticsearch(
        [settings.es_url],
        verify_certs=False
    )
    resp = await es.search (
        index="bongo_data1",
        body={"query": {"match_all": {}}},
        size=20,
    )
    print(resp)
    return await feedCrud.get()

@celery_app.task()
def custom_task():
    print("Hello from celery")
    return True

@celery_app.task()
def custom_task2():
    print("Hello from celery2")
