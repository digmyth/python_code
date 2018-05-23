from celery.result import AsyncResult
from demo.celery import cel

async = AsyncResult(id='0c2a2115-f000-4655-b16d-213c0acc5607',app=cel)
print(async.status)
if async.successful():
    x = async.get()
    print(x)

else:
    print("未执行或执行错误")