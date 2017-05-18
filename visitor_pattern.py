#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'

"""
大话设计模式
设计模式——访问者模式
访问者模式(Visitor Pattern):表示一个作用于某对象结构中的各元素的操作。它使你可以在不改变各元素的类的前提下定义作用于这些元素的新操作
"""
#抽象状态类
class Action(object):

	def get_manconclusion(self,concrete_element):
		pass

	def get_womanconclusion(self,concrete_element):
		pass


#抽象人类
class Person(object):

	def accept(self, visitor):
		pass

#具体状态类—成功
class Success(Action):

	def get_manconclusion(self,concrete_element):
		print concrete_element.__class__.__name__,self.__class__.__name__,"背后多半有一个伟大的女人 "


	def get_womanconclusion(self,concrete_element):
		print concrete_element.__class__.__name__,self.__class__.__name__,"背后大多有一个不成功的男人"

#具体状态类——失败
class Fail(Action):

	def get_manconclusion(self,concrete_element):
		print concrete_element.__class__.__name__,self.__class__.__name__,"闷头喝酒,谁也不用劝 "


	def get_womanconclusion(self,concrete_element):
		print concrete_element.__class__.__name__,self.__class__.__name__,"眼泪汪汪,谁劝也没用"



#具体人类——男人
class Man(Person):

	def accept(self, visitor):
		visitor.get_manconclusion(self)

#具体人类——女人
class Woman(Person):

	def accept(self, visitor):
		visitor.get_womanconclusion(self)

#对象结构类
class Structure(object):

	def __init__(self):
		self.ilist = []

	def attach(self,element):
		self.ilist.append(element)

	def detach(self,element):
		self.ilist.remove(element)

	def display(self,visitor):
		for entry in self.ilist:
			entry.accept(visitor)

if __name__ == "__main__":
	#创建一个对象结构,收集和分派
	structure = Structure()
	man = Man()
	woman = Woman()
	structure.attach(man)
	structure.attach(woman)

	success = Success()
	structure.display(success)
	# 添加一个状态类-Fail 变的很容易
	fail = Fail()
	structure.display(fail)

