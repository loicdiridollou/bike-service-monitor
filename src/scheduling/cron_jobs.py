"""File containing the cron jobs setup"""
from time import sleep
import yaml
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import pandas as pd
from experiments.email_test import email_sender


DEFAULT_CONFIG = "config/config.yaml"

def main_fn(config_fn=DEFAULT_CONFIG):
    """Generator of cron jobs"""
    with open(config_fn, "rb") as config_file:
        cron_times = yaml.full_load(config_file)["cron_times"]

    scheduler = BackgroundScheduler()
    scheduler.start()

    for el in cron_times:
        time = pd.Timestamp(cron_times[el]['time'])
        trigger = CronTrigger(
            hour=time.hour, minute=time.minute, second=time.second, timezone="US/Pacific"
        )
        scheduler.add_job(
            email_sender,
            trigger=trigger,
            kwargs={'stations': cron_times[el]['stations']},
            name=cron_times[el]['name'],
        )

    while True:
        sleep(5)
