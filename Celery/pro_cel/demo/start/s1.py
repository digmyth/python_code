# from demo.task1 import  deploy
from demo.task1 import  f1

result=f1.delay(5,6)
print(result.id)