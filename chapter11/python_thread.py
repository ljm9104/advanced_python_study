import time
import threading

'''
1. 通过Thread类实例化
2. 通过集成Thread来实现多线程，重载run方法
'''


def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")


def get_detail_url(url):
    print("get detail url started")
    time.sleep(4)
    print("get detail url end")


class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url started")
        time.sleep(4)
        print("get detail url end")


if __name__ == "__main__":
    thread1 = threading.Thread(target=get_detail_html, args=("",))
    thread2 = threading.Thread(target=get_detail_url, args=("",))
    # thread1 = GetDetailHtml("get_detail_html")
    # thread2 = GetDetailUrl("get_detail_url")

    # 守护线程，主进程关闭后，子线程也就kill
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)

    start_time = time.time()
    thread1.start()
    thread2.start()

    # 子进程运行完才主进程
    thread1.join()
    thread2.join()

    # 当主线程退出的时候， 子线程kill掉
    print("last time: {}".format(time.time() - start_time))
