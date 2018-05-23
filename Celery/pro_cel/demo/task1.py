from .celery import cel

@cel.task
def f1(x,y):
    print('hello')
    return x + y

@cel.task
def deploy(version,hosts):
    # print('hello')
    return 'doing deploy'