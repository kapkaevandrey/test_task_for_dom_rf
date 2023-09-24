from celery import Celery

from app.core.settings import settings

celery = Celery(__name__)
celery.conf.broker_url = settings.celery_broker_url
celery.conf.result_backend = settings.celery_result_backend

celery.autodiscover_tasks(packages=["app"])
