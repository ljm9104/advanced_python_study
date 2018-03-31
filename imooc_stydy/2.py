#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author:    LJM
# @Date:      2018-03-31 19:03:00

# 如何在list,dict,set中根据条件筛选数据
# 1.迭代
# data = [1, 3, -5, 6, 8, 2]
# res = []
# for i in data:
#     if i > 5:
#         res.append(i)
# print(res)

# 2.函数式编程
# from random import randint
# data = [randint(-10, 10) for _ in range(10)]
# filter_data = filter(lambda x: x>0, data)    # 返回生成器
# print(list(filter_data), filter_data)

# 列表解析
# filter_data2 = [x for x in data if x >= 0]
# print(filter_data2)

# 列表解析和filter时间比较，用timeit


# 1.为每个元祖命名，元祖拆包
# 2.内置collection 模块的namedtuple

# 统计序列中重复出现的频率
# 1.使用字典
# 2.内置collection 模块的Counter
from random import randint
data = [randint(0, 20) for _ in range(10)]
dic = dict.fromkeys(data, 0)
# print(dic)
# 使用迭代
# for x in data:
#     for j in dic.keys():
#         if j == x:
#             dic[j] += 1
# for x in data:
#     dic[x] += 1
# print(dic)  
#  --------------
# from collections import Counter
# dic2 = Counter(dic)
# dic2.most_common(2)
