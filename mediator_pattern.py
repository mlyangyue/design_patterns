#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
大话设计模式
设计模式——中介者模式
中介者模式(Mediator Pattern):用一个对象来封装一系列的对象交互，中介者使各对象不需要显示地相互引用，从而使耦合松散，而且可以独立地改变它们之间的交互.
应用场景:一组已经定义良好但是用复杂的方式进行通信,以及想定制一个分布在多个类中的行为,又不想生成太多子类的场合
(中介者降低交互者的耦合度,并且把交互的中心放在了中介者的身上,站在更宏观的角度上看待系统)
"""
# 抽象中介者类
class Metiator(object):

	def send(self,message,concreteobj):
		pass

# 具体中介者类——联合国
class United(Metiator):

	def __init__(self):
		self.country1 = ""
		self.country2 = ""

	def send(self,message,concreteobj):
		if self.country1 == concreteobj:
			self.country2.get_message(message)
		elif self.country2 == concreteobj:
			self.country1.get_message(message)
		else:
			print '没有对象'
# 抽象交互类
class Country(object):

	def __init__(self):
		self.metiator = ""

	def bind(self,metiator):
		self.metiator = metiator

# 具体交互类——中国
class China(Country):

	def send(self, message):
		self.metiator.send(message,self)

	def get_message(self,message):
		print "中国获取对方消息:",message
# 具体交互类——某国
class Stick(Country):

	def send(self, message):
		self.metiator.send(message,self)

	def get_message(self,message):
		print "棒子获取对方消息:",message


if __name__ == "__main__":
	# 创建中介者,具体的交互者
	united = United()
	china = China()
	stick = Stick()
	# 交互者绑定交互的中介者
	china.bind(united)
	stick.bind(united)

	united.country1 = china
	united.country2 = stick
	#开始交互
	china.send('棒子,别部署萨德,揍你哦')
	stick.send('哥,我错了,不部署了')