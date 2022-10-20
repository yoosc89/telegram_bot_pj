from telegram_alert import alert_bot
from parser_list import parser_db
from pytz import utc
import time


from apscheduler.schedulers.background import BlockingScheduler

def main():
    sched = BlockingScheduler(timezone=utc)
    sched.add_job(parser_db, 'interval',minutes=5, id='parser')
    sched.add_job(alert_bot, 'interval',minutes=2, id='alert')
    sched.start()


if __name__ == '__main__':
    parser_db()
    alert_bot()
    main()
