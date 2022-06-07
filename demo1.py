#coding:utf-8

import psutil

def checkprocess(processname):

    pl = psutil.pids()

    for pid in pl:

        if psutil.Process(pid).name() == processname:

            return pid

# print(isinstance(checkprocess("notepad++.exe"),int))

if isinstance(checkprocess("Yearning"),int):

    print("进程存在")

else:

    print("进程不存在")