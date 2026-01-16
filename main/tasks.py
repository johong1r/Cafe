from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True)
def nums(self):
    n = 0
    while n < 10:
        n += 1
        print(n)
    return n
