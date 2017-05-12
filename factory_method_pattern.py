#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'

"""
大话设计模式

设计模式——工厂方法模式
工厂方法模式(Factory Method Pattern):定义一个用于创建对象的接口,让子类决定实例化哪一个类,工厂方法使一个类的实例化延时到其子类.
工厂方法模式克服了简单工厂模式违背开放-封闭原则的缺点,又保持了封装对象创建过程的优点
场景:雷锋工厂,不关心执行者,只关心执行结果
"""

class LeiFeng(object):

	def Sweep(self):
		print "扫地"

	def Wash(self):
		print "洗衣"

	def BuyRice(self):
		print "买米"


class IFactory(LeiFeng):

	def CreateLeiFeng(self):
		pass

#大学生
class Undergraduate(LeiFeng):
	pass

#新增社区服务者
class Volunteer(LeiFeng):
	pass

# 学习雷锋的大学生工厂
class UndergraduateFactory(IFactory):

	def CreateLeiFeng(self):
		return Undergraduate()

#新增一个社区服务者的工厂
class VolunteerFactory(IFactory):

	def CreateLeiFeng(self):
		return Volunteer()


if __name__ == "__main__":
	student = UndergraduateFactory()
	volunteer = VolunteerFactory()
	student.BuyRice()
	student.Sweep()
	volunteer.Wash()
