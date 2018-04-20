# 内置的上下文管理器
import contextlib


@contextlib.contextmanager
def file_open(file_name):
    print ("file open")
    yield {}        # 生成器
    print ("file end")

with file_open("bobby.txt") as f_opened:
    print ("file processing")
