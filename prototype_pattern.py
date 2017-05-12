#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'

"""
大话设计模式
设计模式——原型模式
原型模式(Prototype Pattern):用原型实例指定创建对象的种类,并且通过拷贝这些原型创建新的对象
原型模式是用场景:需要大量的基于某个基础原型进行微量修改而得到新原型时使用
"""
from copy import copy, deepcopy

# 原型抽象类
class Prototype(object):

	def clone(self):
		pass

	def deep_clone(self):
		pass

# 工作经历类
class WorkExperience(object):

	def __init__(self):
		self.timearea = ''
		self.company = ''

	def set_workexperience(self,timearea, company):
		self.timearea = timearea
		self.company = company


# 简历类   
class Resume(Prototype):

	def __init__(self,name):
		self.name = name
		self.workexperience = WorkExperience()

	def set_personinfo(self,sex,age):
		self.sex = sex
		self.age = age
		pass

	def set_workexperience(self,timearea, company):
		self.workexperience.set_workexperience(timearea, company)

	def display(self):
		print self.name
		print self.sex, self.age
		print '工作经历',self.workexperience.timearea, self.workexperience.company

	def clone(self):
		return copy(self)

	def deep_clone(self):
		return deepcopy(self)


if __name__ == '__main__':
	obj1 = Resume('andy')
	obj2 = obj1.clone()  # 浅拷贝对象
	obj3 = obj1.deep_clone()  # 深拷贝对象

	obj1.set_personinfo('男',28)
	obj1.set_workexperience('2010-2015','AA')
	obj2.set_personinfo('男',27)
	obj2.set_workexperience('2011-2017','AA')  # 修改浅拷贝的对象工作经历
	obj3.set_personinfo('男',29)
	obj3.set_workexperience('2016-2017','AA')  # 修改深拷贝的对象的工作经历


	obj1.display()
	obj2.display()
	obj3.display()



