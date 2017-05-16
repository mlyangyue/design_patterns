#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'

"""
大话设计模式
设计模式——单例模式(Singleton Pattern):保证类仅有一个实例，并提供一个访问它的全局访问点.
(python中模块化的操作,可以代替单例模式,生成一个类的实例作为全局变量,其他地方只引用这个实例就可以实现单例)
"""

#因为__new__在__init__前被执行,利用__new__实现单例

#创建过的单例带有属性__instance
class Singleton1(object):
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls,'__instance'):
			cls.__instance = super(Singleton1, cls).__new__(cls, *args, **kwargs)
			return cls.__instance

#利用__dict__来引用同一个字典
class Singleton2(object):
	_state = {}
	def __new__(cls, *args, **kwargs):
		ob = super(Singleton2, cls).__new__(cls, *args, **kwargs)
		ob.__dict__ = cls._state
		return ob

#利用元类在创建方法时用__metaclass__来创建
class Singleton3(type):

	def __new__(cls, name, bases, dct):
		if not hasattr(cls, '__instance'):
			cls.__instance = super(Singleton3, cls).__new__(cls, name, bases, dct)
			return cls.__instance

#利用装饰器
def singleton4(cls, *args, **kwargs):
	instances = {}
	def _single():
		if cls not in instances:
			instances[cls] = cls(*args, **kwargs)
		return instances[cls]
	return _single



class Myclass1(Singleton1):
	a = 1

class Myclass2(Singleton2):
	a = 2

class Myclass3(object):
	__metaclass__ = Singleton3
	a = 3

@singleton4
class Myclass4(object):
	a = 4

if __name__ == "__main__":
	s1 = Myclass1()
	s2 = Myclass1()
	print s1.a,id(s1.a),id(s2.a) # 1 140630246306072 140630246306072

	s3 = Myclass2()
	s4 = Myclass2()
	print s3.a,id(s3.a),id(s4.a) # 2 140628399791616 140628399791616

	s5 = Myclass3()
	s6 = Myclass3()
	print s5.a,id(s5.a),id(s6.a) # 3 140530304439208 140530304439208

	s7 = Myclass4()
	s8 = Myclass4()
	print s7.a,id(s7.a),id(s8.a) # 4 140684486002032 140684486002032