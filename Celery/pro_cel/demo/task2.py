from  demo.celery import cel

@cel.task
def f2():
    print('world')
    return 'world'