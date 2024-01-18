import time

from celery import shared_task


@shared_task
def mine_bitcoin(time_to_sleep):
    time.sleep(time_to_sleep)
    return time_to_sleep + 100
