import datetime
from flask import Flask,render_template,request,redirect
from celery.result import AsyncResult
from demo.celery import cel
from demo.task1 import deploy
hist = []
app = Flask(__name__)

@app.route('/index',methods=['GET','POST'])
def index():
    return render_template('index.html',hist=hist)

@app.route('/publish',methods=['GET','POST'])
def publish():
    if request.method == 'GET':
        return render_template('deploy.html')
    elif request.method == 'POST':
        version = request.form.get('version')
        hosts = request.form.getlist('hosts')
        print(version,hosts)
        ctime = datetime.datetime.now()
        utc_time = datetime.datetime.utcfromtimestamp(ctime.timestamp())
        ctime_10 = utc_time + datetime.timedelta(seconds=3)
        result = deploy.apply_async(args=[version,hosts,],eta=ctime_10)
        print(result.id)
        hist.append({'version':version,'hosts':hosts,'task_id':result.id})

        return redirect('/index')

@app.route('/check_result')
def check_result():
    task_id = request.args.get('task_id')
    print(task_id)
    async = AsyncResult(id=task_id,app=cel)
    print(async.status)
    if async.successful():
        result = async.get()
        print(result)
        async.forget() # 将结果删除
        return '执行成功'
    elif async.failed():
        return '执行失败'
    elif async.status == 'PENDING':
        return  '任务等待被执行中'
    elif async.status == 'RETRY':
        return '任务异常后正在重试'
    elif async.status == 'STARTED':
        return '任务已经开始被执行'
    else:
        return '未知错误'

@app.route('/cancel')
def cancel():
    task_id = request.args.get('task_id')
    async = AsyncResult(id=task_id, app=cel)
    async.revoke(terminate=True)

    for i in hist:
        for k, v in i.items():
            if v == task_id:
                hist.remove(i)
                break

    return redirect('/index')

if __name__ == '__main__':
    app.run(threaded=True)