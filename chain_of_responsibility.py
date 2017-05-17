#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
大话设计模式
设计模式——职责链模式
职责链模式(Chain Of Responsibility):使多个对象都有机会处理请求，从而避免发送者和接收者的耦合关系。将对象连成链并沿着这条链传递请求直到被处理
(在调用时要定义好哪个实例是哪个实例的职责上一级)
"""
#抽象一个处理类
class Handle(object):

	def __init__(self):
		self.successor = ''

	def setsuccessor(self, successor):
		self.successor = successor

	def handle_request(self,request):
		pass

# 具体处理者类1
class ConcreteHandle1(Handle):

	def handle_request(self,request):
		if request>0 and request<=10:
			print "ConcreteHandle1处理请求 ",request
		else:
			self.successor.handle_request(request)

# 具体处理者类2
class ConcreteHandle2(Handle):

	def handle_request(self,request):
		if request>10 and request<=20:
			print "ConcreteHandle2处理请求 ",request
		else:
			self.successor.handle_request(request)

if __name__=="__main__":
	c1 = ConcreteHandle1()
	c2 = ConcreteHandle2()
	c1.setsuccessor(c2)

	for i in range(6,15,2):
		c1.handle_request(i)