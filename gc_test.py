#coding=utf8

import sys
import gc
import time

class ClassA():
    def __init__(self):
        '''初始化对象'''
        print('object born id:%s' %str(hex(id(self))))

    def __del__(self):
        print 'object del,id:%s'%str(hex(id(self)))


def f3():
    c1=ClassA()
    c2=ClassA()
    c1.t=c2
    c2.t=c1
    del c1
    del c2
    print gc.garbage
    print gc.collect() #显式执行垃圾回收
    print gc.garbage
    time.sleep(10)

if __name__ == '__main__':
    f3()