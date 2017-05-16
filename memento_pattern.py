#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
大话设计模式
设计模式——备忘录模式
备忘录模式(Memento Pattern):不破坏封装性的前提下捕获一个对象的内部状态，并在该对象之外保存这个状态,这样已经后就可将该对象恢复到原先保存的状态
"""

# 发起人类
class Originator(object):

    def __init__(self, state):
        self.state = state

    def create_memento(self):
        return Memento(self.state)

    def set_memento(self, memento):
        self.state = memento.state

    def show(self):
        print "当前状态 ", self.state

# 备忘录类
class Memento(object):

    def __init__(self, state):
        self.state = state

# 管理者类
class Caretaker(object):

    def __init__(self,memento):
        self.memento = memento



if __name__ == "__main__":
    # 初始状态
    originator = Originator(state='On')
    originator.show()
    # 备忘录
    caretaker = Caretaker(originator.create_memento())
    # 修改状态
    originator.state = 'Off'
    originator.show()
    # 复原状态
    originator.set_memento(caretaker.memento)
    originator.show()








