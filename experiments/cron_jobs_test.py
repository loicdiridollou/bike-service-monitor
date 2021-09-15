from time import sleep

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from experiments.email_test import email_sender

def main_fn():
    scheduler = BackgroundScheduler()
    scheduler.start()

    trigger = CronTrigger(
        hour="6", minute="20", second="0", timezone="US/Pacific"
    )
    scheduler.add_job(
        email_sender,
        trigger=trigger,
        name="daily foo",
    )
    while True:
        sleep(5)
