from fastapi import APIRouter

from app.heroes.api import router as heroes_router
from app.search.api import router as search_router
from app.feed.api import router as feed_router

api_router = APIRouter()

include_api = api_router.include_router

routers = (
    (heroes_router, "heroes", "heroes"),
    (search_router, "search", "search"),
    (feed_router, "feed", "feed"),
)

for router_item in routers:
    router, prefix, tag = router_item

    if tag:
        include_api(router, prefix=f"/{prefix}", tags=[tag])
    else:
        include_api(router, prefix=f"/{prefix}")
