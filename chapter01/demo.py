#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author:    LJM
# @Date:      2018-04-21 21:43:17
import os

rpid = os.fork()
if rpid<0:
    print("fork调用失败。")
elif rpid == 0:
    print("我是子进程（%s），我的父进程是（%s）"%(os.getpid(),os.getppid()))
    x+=1
else:
    print("我是父进程（%s），我的子进程是（%s）"%(os.getpid(),rpid))

print("父子进程都可以执行这里的代码")