my_list = []
my_list.append(1)
my_list.append("a")

from collections import abc

a = [1,2]
c = a + [3,4]

'''
+ 与 += 与 extend区别以及append
+ 相加两侧数据类型一致
+= 两侧
'''
# 就地加
# a += (3,4)
# a.extend(range(3))

a.append((1,2))
print(a)