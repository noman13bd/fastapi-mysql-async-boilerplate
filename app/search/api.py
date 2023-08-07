from fastapi import APIRouter, Depends
from fastapi import status as http_status

router = APIRouter()

@router.get(
    "",
    status_code=http_status.HTTP_200_OK
)
async def get_search_results():
    return { "head": "search" }