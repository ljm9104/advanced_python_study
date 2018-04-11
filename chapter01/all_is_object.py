"""
一切皆对象
1. 赋值给一变量
2. 可以添加到集合对象
3. 可以作为参数传递，
4. 可以作为函数返回值 （装饰器，闭包，递归中）
"""


# 函数作为对象
def ask(name="ljm"):
    print(name)


func = ask
func("ming")


# 类作为对象
class Person:
    def __init__(self):
        print("ming")


my_class = Person
my_class()
