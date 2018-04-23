# 上下文管理器协议，实现了__enter__和__exit__魔法函数
class Sample:
    def __enter__(self):
        print ("enter")
        # 获取资源
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print ("exit")
    def do_something(self):
        print ("doing something")

with Sample() as sample:
    sample.do_something()


# 内置的上下文管理器,yield前面__enter__，后面__exit__
import contextlib


@contextlib.contextmanager
def file_open(file_name):
    print ("file open")
    yield {}                # 生成器
    # yield 123                
    print ("file end")

with file_open("bobby.txt") as f_opened:
    print ("file processing")
print(f_opened)
