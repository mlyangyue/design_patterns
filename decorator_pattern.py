#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'

"""
大话设计模式

设计模式——装饰模式
装饰模式(Decorator Pattern):动态的给一个对象添加一些额外的职责,就增加功能来说,装饰模式比生成子类更为灵活.
特点: 有效的把类的核心职责和装饰功能区分开,而且可以去除相关类中重复的装饰逻辑
"""

# 定义对象接口
class Person(object):

	def __init__(self,name):
		self.name = name

	def show(self):
		print "装扮的%s"%self.name

#装饰类
class Finery(Person):

	def __init__(self):
		pass

	def Decorate(self,componet):
		self.componet = componet

	def show(self):
		if self.componet != None:
			self.componet.show()

#装扮——T恤
class TShirts(Finery):

	def __init__(self):
		pass

	def show(self):
		print 'T恤'
		self.componet.show()

#装扮——大裤衩
class BigTrouser(Finery):

	def __init__(self):
		pass

	def show(self):
		print '大裤衩'
		self.componet.show()

# 装扮——人字拖
class FlipFlops(Finery):

	def __init__(self):
		pass

	def show(self):
		print '人字拖'
		self.componet.show()

if __name__ == '__main__':
	p = Person('Andy')
	ff = FlipFlops()
	bt = BigTrouser()
	ts = TShirts()
	ff.Decorate(p)
	bt.Decorate(ff)
	ts.Decorate(bt)
	ts.show()