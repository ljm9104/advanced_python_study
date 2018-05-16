import time
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
from concurrent.futures import Future
from multiprocessing import Pool


def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=2)
# 通过submit函数提交执行的函数到线程池中, submit 是立即返回
task1 = executor.submit(get_html, (3))
task2 = executor.submit(get_html, (2))

# 要获取已经成功的task的返回
urls = [3, 2, 4]
all_task = [executor.submit(get_html, (url)) for url in urls]
wait(all_task, return_when=FIRST_COMPLETED)
print("main")
for future in as_completed(all_task):
    data = future.result()
    print("get {} page".format(data))
# 通过executor的map获取已经完成的task的值
for data in executor.map(get_html, urls):
    print("get {} page".format(data))

# done方法用于判定某个任务是否完成
print(task1.done())
print(task2.cancel())
time.sleep(3)
print(task1.done())

# result方法可以获取task的执行结果
print(task1.result())
