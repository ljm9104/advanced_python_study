import threading

# import dis
# def add(a):
#   a = a+1
#   return a
# print(dis.dis(add))

'''
GIL 会根据执行的字节码行数以及时间片释放GIL ，GIL 在遇到io的操作时候主动释放
    # 1. dosomething1
    # 2. io操作
    # 1. dosomething3
'''

total = 0


def add():
    global total
    for i in range(1000000):
        total += 1


def desc():
    global total
    for i in range(1000000):
        total -= 1


thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)
