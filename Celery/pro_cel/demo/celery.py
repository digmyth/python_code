
from celery import Celery

cel = Celery(__name__,
             broker='redis://192.168.1.8:6379',
             backend='redis://192.168.1.8:6379',
             include=['demo.task1','demo.task2'])