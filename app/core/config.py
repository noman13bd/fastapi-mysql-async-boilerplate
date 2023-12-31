""" App Settings """
from pydantic import BaseSettings


class Settings(BaseSettings):
    """App Settings class"""

    # Base
    api_v1_prefix: str
    debug: bool
    project_name: str
    version: str
    description: str

    # Database
    db_async_connection_str: str
    db_async_test_connection_str: str
    celery_broker_url: str
    es_url: str
