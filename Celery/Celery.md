# Celery入门学习

官方推荐broker是rabbitmq,当然也可以用redis

[参考1](http://www.cnblogs.com/wupeiqi/articles/8796552.html)

[参考2](https://www.cnblogs.com/alex3714/p/6351797.html)

## 安装celery
celery 4.0以上不支持windows,为测试方便我安装低版本
```
pip3 install celery==3.1.25
pip3 install eventlet  # 仅需windows时
```

## 快速入门
```
#s1.py
from celery import Celery

cel = Celery('task',
             broker='redis://192.168.1.8:6379',
             backend='redis://192.168.1.8:6379',)

@cel.task
def f1(x,y):
    return x+y
```

```
#s2.py
from s1 import f1

result = f1.delay(5,8)
print(result.id)
```

```
#s3.py
from celery.result import AsyncResult
from s1 import cel

async = AsyncResult(id='3026605c-3a8a-4e94-b514-d68e166460d2',app=cel)

print(async.status)
if async.successful():
    print(async.get())
elif async.failed():
    print('执行失败')
elif async.status == 'PENDING':
    print('任务等待中被执行')
elif async.status == 'RETRY':
    print('任务异常后正在重试')
elif async.status == 'STARTED':
    print('任务已经开始被执行')
```

运行测试代码
```
celery worker -A s1 -l info -P eventlet
python3 s2.py  # 得到ID
python3 s3.py  # 根据ID取出结果
```

## 结构化目录

```
xx
```

