import datetime
import logging

from apscheduler.schedulers.background import BackgroundScheduler


logger = logging.getLogger(__name__)

def my_task():
    print("TASK:", datetime.datetime.now())
    # logger.info("TASK: %s", datetime.datetime.now())
    # from apps.core.services.currency_service import CurrencyService
    # print("USD:", CurrencyService.get_usd_rate())

def start():
    print("START")
    my_task()
    scheduler = BackgroundScheduler(timezone="Europe/Kyiv")
    # Для збереження задач в DB, не працює з SQLite (PostgreSQL)
    # scheduler.add_jobstore(DjangoJobStore(), "default")
    # scheduler.add_job(my_task, "interval", minutes=1, id="my_task", replace_existing=True)
    scheduler.add_job(my_task, "interval", seconds=30, id="my_task", replace_existing=True)
    scheduler.start()
    print("Planner RUNNING")
    # logger.info("Planner RUNNING")