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

redis基于存取数据机制，可以做双向队列（先进先出）和栈（先进后出）
```
# pip3 install redis
import redis

conn = redis.Redis(host='192.168.109.144',port=6379)

# conn.lpush('user','u1')
# conn.rpush('user','u2')
# t = conn.brpop('user',timeout=3) # b表示block,没有取到会有超时时间，返回元组
# print(t)
```

如果预先存了n个值,我们总不能一次性取出吧，那样会占用大量内存，我们可以循环一次取出100个值，再在100个值中循环取来用
```
# conn.lpush('user','u1')
# conn.rpush('user','u2')
# conn.rpush('user','u3')
# conn.rpush('user','u4')
# conn.rpush('user','u5')
# conn.rpush('user','u6')
# conn.rpush('user','u7')
# conn.rpush('user','un')
```
那么相关代码就是
```
def list_scan_iter(name):
    '''
    注意： 只是根据索引查看队列里面的数据，并未取出
    '''
    start = 0
    while True:
        vals = conn.lrange(name, start, start+100)
        start = start + 101
        if not vals:
            return
        for val in vals:
            yield val    # val是什么，后面for中i就是什么

for i in list_scan_iter('user'):
    print(i,)
```


