from fastapi import APIRouter, Depends
from fastapi import status as http_status
from app.core.celery_conf import celery_app

router = APIRouter()

@router.get(
    "",
    status_code=http_status.HTTP_200_OK
)
async def get_search_results():
    test_q_task.delay()
    return { "head": "search" }

@celery_app.task
def test_q_task():
    print("Testing")
