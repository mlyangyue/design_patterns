#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
大话设计模式
设计模式——模板方法模式
模板方法模式(Template Method Pattern):定义一个操作中的算法骨架，将一些步骤延迟至子类中.模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤
使用场景:当不变和可变的行为在方法的子类实现中混合在一起时,不变的行为就会在子类中重复出现，用模板方法模式把这些不变的行为搬到单一的地方,帮助子类摆脱重复不变的行为纠缠
"""

class NewPaper(object):

	def question1(self):
		print "题目1"
		print self.answer1()

	def question2(self):
		print "题目2"
		print self.answer2()

	def answer1(self):
		return ''

	def answer2(self):
		return ''


class TestPaperA(NewPaper):

	def answer1(self):
		return '答案A1'

	def answer2(self):
		return '答案A2'


class TestPaperB(NewPaper):

	def answer1(self):
		return '答案B1'

	def answer2(self):
		return '答案B2'


if __name__ == '__main__':
	test1 = TestPaperA()
	test2 = TestPaperB()
	print "试卷A"
	test1.question1()
	test1.question2()
	print "试卷B"
	test2.question1()
	test2.question2()

