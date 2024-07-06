"""File containing the cron jobs setup."""

from pathlib import Path
from time import sleep

import pandas as pd
import yaml
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from bms.mailing.sender import email_sender

DEFAULT_CONFIG = Path("config/config.yaml")


def main_fn(config_fn=DEFAULT_CONFIG):
    """Generate method for ron jobs."""
    with config_fn.open("rb") as config_file:
        cron_times = yaml.full_load(config_file)["cron_times"]

    scheduler = BackgroundScheduler()
    scheduler.start()

    for ele in cron_times:
        time = pd.Timestamp(cron_times[ele]["time"])
        trigger = CronTrigger(
            hour=time.hour,
            minute=time.minute,
            second=time.second,
            day_of_week=cron_times[ele]["day_of_week"],
            timezone="US/Pacific",
        )
        scheduler.add_job(
            email_sender,
            trigger=trigger,
            kwargs={"stations": cron_times[ele]["stations"].split(",")},
            name=cron_times[ele]["name"],
        )

    while True:
        sleep(5)
