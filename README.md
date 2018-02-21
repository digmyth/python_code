# python_code 代码片段


satisfied with the Python development

## 
```
import types

class Foo():
    def f1(self):
        print('f1')
obj = Foo()
def f2(self):
    print('f2')

isinstance(Foo.f1, types.FunctionType)  # True Foo.f1是函数
isinstance(f2, types.FunctionType)      # True
isinstance(obj.f1, types.MethodType)    # True obj.f1是绑定方法
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
    x()
else:
    setattr(obj,choice,func2)
    x=getattr(obj,choice)
    print(x)
    x(obj)
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
