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

isinstance(Foo.f1, types.FunctionType)  # True Foo.f1是函数
isinstance(f2, types.FunctionType)      # True
isinstance(obj.f1, types.MethodType)    # True obj.f1是绑定方法
```


```
type(fn)==types.FunctionType
type(abs)==types.BuiltinFunctionType
type(lambda x: x)==types.LambdaType 
type((x for x in range(10)))==types.GeneratorType
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
