class A:
    aa = 1
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = A(2,3)

A.aa = 11
a.aa = 100
print(a.x, a.y, a.aa)
print(A.aa)
print(A.__dict__, a.__dict__,sep='\n')

b = A(3,5)
print(b.aa)

'''
变量查找规则LEGB
代表名字查找顺序: locals -> enclosing function -> globals -> __builtins__
    locals      是函数内的名字空间，包括局部变量和形参
    enclosing   外部嵌套函数的名字空间（闭包中常见）
    globals     全局变量，函数定义所在模块的名字空间
    builtins    内置模块的名字空间
'''