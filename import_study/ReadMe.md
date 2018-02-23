# Python基础知识之import模块导入

这里主要学习import/from...import细节上的东西，对于刚入门开发的小白来说还是很重要的，大神就先跳过，知道看不上

## 模块导入
* __all__ 只用于from xx import * 形式导入起限定作用,记住有星

1 在定义一个模块时如md.py,写入了很多语句或变量,__all__可以限定别人from导入模块哪些变量或方法
 ```
 __all__ = ['x','func']
    x=1
    y=2
    def func():
        pass
```
2 在一个一个多级目录包下有很多模块时，别人from xx import * (只有from)导入可能找不到模块，这时可以在各个包的__init__.py文件里定义__all__指定包下哪些模块可以导入，有时问题得到解决.
问题： any.py里找不到c包
```
from app01.a.b import *

def func():
    return  c.c1.AdminSite()

x=func()
print(x)
```
解决：b包目录__init__.py定义__all__
```
__all__ = ['c',] # 在这种情况下__all__有着from app01.a.b import c 相同作用
```


3 只要导入（impor或from import）就会从上到下执行各个包的__init__.py文件，一般__init__.py文件定义该包下的模块导入. 
比如a包有b,c模块,那么a的__init__.py文件可以定义为from a import b,c

## 简单示例

看一个简单示例

lib/conf/global_settings.py
```
NAME = 'wxq'
ENGINE = 'engine.get_session'
xxx = 'xxxx4'
```

lib/conf/__init__.py
```
# from . import global_settings
from  .global_settings import xxx

class Settings():
    def __init__(self):
        for item in dir(global_settings):
            if item.isupper():
                item_value=getattr(global_settings,item)
                print(item_value)

settings = Settings()
```

test.py
```
# from lib.conf import settings
from lib.conf import xxx
print(xxx)
```

## 总结

在大多数情况下都需要在各个包__init__.py下定义from xx import xx来初始化包路径

