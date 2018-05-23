# ReadMe

demo目录可以随意命名，可改为celery_tasks,demo目录可单独运行，是完整的celery结构化目录结构
### 测试步骤

```
1. celery worker -A demo -l info -P eventlet
# 2. python3 start/s1.py # 得到ID
# 3. python3 start/s2.py # 根据ID取得结果
2.Flask app启动：http://127.0.0.1:5000/publish
```
