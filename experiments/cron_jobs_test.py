from time import sleep

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from experiments.email_test import email_sender

def main_fn():
    scheduler = BackgroundScheduler()
    scheduler.start()

    trigger1 = CronTrigger(
        hour="20", minute="56", second="0", timezone="US/Pacific"
    )
    trigger2 = CronTrigger(
        hour="6", minute="22", second="0", timezone="US/Pacific"
    )
    scheduler.add_job(
        email_sender,
        trigger=trigger1,
        name="Morning run",
    )
    scheduler.add_job(
        email_sender,
        trigger=trigger2,
        name="Evening run",
    )
    while True:
        sleep(5)
