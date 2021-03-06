"""
with语句上下文管理协议实现__enter__和__exit__魔法函数

try except finally

return语句执行，若finaly里有return执行，若没有就执行之前
"""

def exe_try():
    try:
        print ("code started")
        raise KeyError
        return 1
    except KeyError as e:
        print ("key error")
        return 2
    else:
        print ("other error")
        return 3
    finally:
        print ("finally")
        # return 4           # return语句执行顺序，finaly没有return执行前面的，有就执行finaly的


# 上下文管理器协议
# class Sample:
#     def __enter__(self):
#         print ("enter")
#         # 获取资源
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         # 释放资源
#         print ("exit")
#     def do_something(self):
#         print ("doing something")

# with Sample() as sample:
#     sample.do_something()

if __name__ == "__main__":
    result = exe_try()
    print (result)

