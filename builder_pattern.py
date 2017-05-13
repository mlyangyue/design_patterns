#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'

"""
大话设计模式
设计模式——建造者模式
建造者模式(Builder):将一个复杂对象的构建与它的表示分离,使得同样的构建过程可以常见不同的表示
特性: 指挥者(Director) 指挥 建造者(Builder) 建造 Product
"""

class Builder(object):

	def create_header(self):
		pass

	def create_body(self):
		pass

	def create_hand(self):
		pass

	def create_foot(self):
		pass

class Thin(Builder):

	def create_header(self):
		print '瘦子的头'

	def create_body(self):
		print '瘦子的身体'

	def create_hand(self):
		print '瘦子的手'

	def create_foot(self):
		print '瘦子的脚'

class Fat(Builder):

	def create_header(self):
		print '胖子的头'

	def create_body(self):
		print '胖子的身体'

	def create_hand(self):
		print '胖子的手'

	def create_foot(self):
		print '胖子的脚'

class Director(object):

	def __init__(self, person):
		self.person = person

	def create_preson(self):
		self.person.create_header()
		self.person.create_body()
		self.person.create_hand()
		self.person.create_foot()


if __name__=="__main__":
	thin = Thin()
	fat = Fat()
	director_thin = Director(thin)
	director_fat = Director(fat)
	director_thin.create_preson()
	director_fat.create_preson()
