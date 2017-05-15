#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
大话设计模式
设计模式——适配器模式
适配器模式(Adapter Pattern):将一个类的接口转换成为客户希望的另外一个接口.Adapter Pattern使得原本由于接口不兼容而不能一起工作的那些类可以一起工作.
应用场景:系统数据和行为都正确,但接口不符合时,目的是使控制范围之外的一个原有对象与某个接口匹配,适配器模式主要应用于希望复用一些现存的类,但接口又与复用环境不一致的情况
"""
class Target(object):

	def request(self):
		print "普通请求"

class Adaptee(object):

	def specific_request(self):
		print "特殊请求"

class Adapter(Target):

	def __init__(self):
		self.adaptee = Adaptee()

	def request(self):
		self.adaptee.specific_request()

if __name__ == "__main__":
	target = Adapter()
	target.request()


