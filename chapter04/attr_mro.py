#新式类
"""
新式类算法--MR算法，深度优先
"""
class D(object):
    pass

class E:
    pass

class C(E):
    pass

class B(D):
    pass

class A(B, C):
    pass

print(A.__mro__)
