"""
with语句上下文管理协议实现__enter__和__exit__魔法函数

try except else finally

return语句执行，若finaly里有return执行finally里面的，若没有就执行之前，try，except，else
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
        # return 4           # return语句执行顺序，finally没有return执行前面的，有就执行finaly的


if __name__ == "__main__":
    result = exe_try()
    print (result)

