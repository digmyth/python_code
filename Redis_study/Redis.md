## redis基础知识

redis 5大数据类型： 字符串，列表，字典，集合，有序集合

```
pip3 install redis
apt-get install redis-server  # on ubuntu 14.04
service redis-server start
```

创建连接
```
import redis

pool = redis.ConnectionPool(host='192.168.1.8',port=6379,max_connections=50)
conn = redis.Redis(connection_pool=pool)
conn.set('k1','v1')
v=conn.get('k1')
```

字符串类型快速上手
```
conn = redis.Redis(host='192.168.1.8',port=6379)
conn.set('k1','xxxxx')
v=conn.get('k1')
print(v)   # 字节
conn.delete('k1')     # 删除
```

字典数据类型快速上手，(hash)
```
conn = redis.Redis(host='192.168.1.8',port=6379)
conn.hset('sdgasdf','is_login','true')    # 'sdgasdf'为随机字串用于hash,'is_login','true'才是我们真正存的数据
conn.expire('sdgasdf',5)     # 设置超时时间
v=conn.hget('sdgasdf','is_login')
print(v)
conn.hdel('sdgasdf','is_login')
```

表判断
```
v=conn.hget('sdgasdf','is_login')  # 取'is_login'键存不存在值
v=conn.exists('sdgasdf')           # 取外层键'sdgasdf'存不存在
```


