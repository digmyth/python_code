# python_code 代码片段


satisfied with the Python development

## types

types.FunctionType/types.MethodType道出函数和类方法的区别，如果是函数，self参数手动传入.如果是绑定方法，self参数不用传，自动把对象传入self
```
import types

class Foo():
    def f1(self):
        print('f1')
obj = Foo()
def f2(self):
    print('f2')

isinstance(Foo.f1, types.FunctionType)  # True (Foo.f1是函数)
isinstance(f2, types.FunctionType)      # True (f2肯定是函数)
isinstance(obj.f1, types.MethodType)    # True (obj.f1是绑定方法，不是函数)
```

有时写代码会用到如下判断
```
type(fn)==types.FunctionType       # 返回True
type(abs)==types.BuiltinFunctionType  # 返回True
type(lambda x: x)==types.LambdaType   # 返回True
type((x for x in range(10)))==types.GeneratorType   # 返回True
```


## type()

类是程序运行时动态创建的，那么是谁创建了类呢，答案是type()函数，type()函数既可以返回一个对象的类型，又可以创建出新的类型.
通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class

要创建一个class对象，type()函数依次传入3个参数：
```
1 class的名称；
2 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3 class的方法名称与函数绑定，这里我们把函数f1绑定到方法名func上,调用时obj.func()
```

示例
```
def f1(self):
    print('test func')

Foo = type('Foo',(object,), {'func':f1})
obj = Foo()
obj.func()
print(obj.func)  # 真正绑定，是类的绑定方法
```


当然了，setattr反射机制也可以动态加载一个函数,但不是类的绑定方法
```
class Foo():
    pass

def func(self):
    print('test func')

obj = Foo()
setattr(obj,'func', func)
f=getattr(obj,'func')
f(obj)
```


## getattr setattr delattr
```
class Foo():
    def __init__(self):
        self.name = 'wxq'

    def func1(self):
        print('func1')

def func2(self):
    print('func2')

obj = Foo()
choice = input(">>>")

if hasattr(obj,choice):
    x=getattr(obj,choice)
    print(x)
    x()       # 绑定方法调用时自动传入self
else:
    setattr(obj,choice,func2)
    x=getattr(obj,choice)
    print(x)
    x(obj)    #  函数调用时手动传入self
```

## getitem setitem delitem
```
class Foo():
    def __init__(self,attrs={}):
        print("init")
        self.attrs =attrs

    def __getitem__(self, item):
        print("get")
        return self.attrs.get(item)

    def __setitem__(self, key, value):
        print("set")
        self.attrs[key] = value

    def __delitem__(self, key):
        print("del")
        del self.attrs[key]

obj = Foo()
obj['name'] = 'wxq'
print(obj['name'])
```

## 正则分组
```
import re
p = re.compile(r'(.*)/id\-(.*)')

random_str = 'sfdasdfsd/id-xxxxxet'
ret = p.findall(random_str)
print(ret[0][0])
print(ret[0][1])
```

## zip

```
a = ["k1","k2","k3","k4"]
b = ["v1","v2","v3","v4"]

dic = {}
L = []
for k,v in zip(a,b):
    dic['name'] = k
    dic['uuid'] = v
    L.append(dic)
    dic = {}
print(L)    
```

## hashlib生成随机字符串
hashlib.md5()生成随机字符串
```
import hashlib
def gen_random_str():
    md5 = hashlib.md5()
    md5.update(str(time.time()).encode("utf-8"))
    return md5.hexdigest()

print(gen_random_str())
```

hashlib.sha1()也可以生成随机字符串，不过没有安全性，己经被破解,openstack/nova/_base/xxxx就是基于镜像ID+sha1生成的
```
import hashlib
image_id = 'xxxxxxxxxxxx'
x = hashlib.sha1()
x.update(image_id.encode())
print(x.hexdigest())
```

写成一行
```
x=hashlib.sha1("xx".encode()).hexdigest()
```

## uuid 生成随机字符串
```
import uuid
x=uuid.uuid1()
print(x)
```

## json序列化

我们都知道json.dumps()序列化后格式为""的字符串
```
import json
dic = {'name':'wxq','age':25}
d=json.dumps(dic)
print(d)  # {"name": "wxq", "age": 25}
```

那么能json.loads()的一定是""的字符串
```
import json
s= "sdfdf"
json.loads(s)  # 肯定会报错，因为s其实是sdfdf
```

正确姿势除了正常json.dumps()外，还可以
```
import json
s= '"sdfdf"'
x=json.loads(s)
print(type(x), x)  # <class 'str'> sdfdf
```

# 类的一点点

类对象调用方法时永选先从自己类查找，然后才是查找父类，这一点很重要
```
def func():
    pass

x=func
import types
a=isinstance(x,types.FunctionType)
print(a)  # 判断一个字符串是不是函数
```

```
class Foo():
    def __init__(self,name,age):
        self.name = name
        self.age = age
obj = Foo("wxq",18)
x="name"

a=getattr(obj,x, "NotFound") # 通过字符串获取属性(反射)
print(a)
```

```
class A():
    def func1(self):
        return self.func2()

    def func2(self):
        print("A.func2")

class B(A):
    def func2(self):
        print("B.func2")

obj=B()
obj.func1()   # 这里打印"B.func2",也就是说先从调用对象找起
```


`__getattr__` `__setattr__`
```
class Foo():
    def __init__(self):
        self.name = 'aaa' # 本来是可以设置值的，但有__setattr__拦截并pass掉，意味着没有赋上属性

    def __getattr__(self, item):
        return 'xxx'

    def __setattr__(self, key, value):
        pass

obj = Foo()
obj.name = 'wxq'    # 本来是可以设置值的，但有__setattr__拦截并pass掉，意味着没有赋上属性
print(obj.name)     # 当没有name属性时，执行__getattr__
```


## get_local ip address

```
#!/usr/bin/env python3

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8',80))
ip = s.getsockname()[0]
print(ip)
```

## convert netmask into num
```
#!/usr/bin/env python3

netmask = '255.255.240.0'
result = ""
print(netmask)
for num in netmask.split('.'):
  temp = str(bin(int(num)))[2:]
  result = result + temp
print(len("".join(str(result).split('0')[0:1])))
```
