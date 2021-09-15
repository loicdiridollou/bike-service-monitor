from time import sleep

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from experiments.email_test import email_sender

def main_fn():
    scheduler = BackgroundScheduler()
    scheduler.start()

    trigger = CronTrigger(
        second="0,30"
    )
    scheduler.add_job(
        email_sender,
        trigger=trigger,
        name="daily foo",
    )
    while True:
        sleep(5)
