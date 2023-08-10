""" Celery Setup """
from celery import Celery
from app import settings

celery_app = Celery(
    "tasks",
    broker=settings.celery_broker_url,
    include=["app.feed.api", "app.search.api"],
)
celery_app.conf.timezone = "Asia/Dhaka"
