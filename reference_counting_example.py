#coding=utf8

import sys
class ClassA():
    def __init__(self):
        '''初始化对象'''
        print('object born id:%s' %str(hex(id(self))))

    def __del__(self):
        print 'object del,id:%s'%str(hex(id(self)))


def func(c):
    print('obejct refcount is: ',sys.getrefcount(c)) #getrefcount()方法用于返回对象的引用计数


def func1(c,d):
     print 'in func function', sys.getrefcount(c)

def f1():
    while True:
        c1 = ClassA()
        c2 = ClassA()
        del c1
        del c2

if __name__ == '__main__':
    # f1()

     print 'init', sys.getrefcount(11)
     a = 11
     print 'after a=11', sys.getrefcount(11)
     b = a
     print 'after b=1', sys.getrefcount(11)
     func(11)
     print 'after func(a)', sys.getrefcount(11)
     list1 = [a, 12, 14]
     print 'after list1=[a,12,14]', sys.getrefcount(11)
     a=12
     print 'after a=12', sys.getrefcount(11)
     del a
     print 'after del a', sys.getrefcount(11)
     del b
     print 'after del b', sys.getrefcount(11)
     # list1.pop(0)
     # print 'after pop list1',sys.getrefcount(11)-1
     del list1
     print 'after del list1', sys.getrefcount(11)