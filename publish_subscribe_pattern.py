#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'

"""
大话设计模式
设计模式——观察者模式
观察者模式又叫做发布-订阅模式 (Publish Subscribe Pattern):定义了一种一对多的关系，让多个观察对象同时监听一个主题对象，当主题对象状态发生变化时会通知所有观察者,是它们能够自动更新自己
使用场景:当一个对象的改变需要同时改变其他对象的时候,而且它不知道具体有多少对象待改变
"""

#抽象通知者类
class Subject(object):

	def attach(self, observer):
		pass

	def detach(self,observer):
		pass

	def notify(self):
		pass


#具体通知者类
class Boss(Subject):

	def __init__(self):
		self.observer_list = []
		self.subject_status = ''

	def attach(self, observer):
		self.observer_list.append(observer)

	def detach(self,observer):
		self.observer_list.remove(observer)

	def notify(self):
		for item in self.observer_list:
			item.update()

#抽象观察者类
class Observer(object):

	def __init__(self, name, publish):
		self.name = name
		self.publish = publish

	def update(self):
		pass

#具体观察者类-看股票的人
class StockObserver(Observer):

	def update(self):
		print self.publish.subject_status,self.name,'关闭股票行情,继续工作'


#具体观察者类-看NBA的人
class NbaObserver(Observer):

	def update(self):
		print self.publish.subject_status,self.name,'关闭NBA,继续工作'


if __name__ == "__main__":
	publisher = Boss()
	stocker = StockObserver('Andy',publisher)
	nbaer = NbaObserver('Tracy',publisher)
	publisher.attach(stocker)
	publisher.attach(nbaer)
	publisher.subject_status = '本老板回来了'
	publisher.notify()