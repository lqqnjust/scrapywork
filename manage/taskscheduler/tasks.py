import time

def task1():
    print(time.time())



from apscheduler.schedulers.background import BackgroundScheduler
import time
from taskscheduler.tasks import task1

scheduler = BackgroundScheduler()

def init():
    scheduler.add_job(task1, 'interval', seconds=5)
    scheduler.start()

