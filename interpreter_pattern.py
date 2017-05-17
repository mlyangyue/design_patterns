#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
大话设计模式
设计模式——解释器模式
解释器模式(Interpreter Pattern):给定一个语言，定义它的文法的一种表示，并定义一个解释器，这个解释器使用该表示来解释语言中的句子.
"""
#抽象一个解释器类
class AbstractExpression(object):

	def interpreter(self, context):
		pass

#具体解释器——终端 继承抽象解释器
class TerminalExpression(AbstractExpression):

	def interpreter(self, context):
		print "终端解释器",context

#具体解释器——终端 继承抽象解释器
class NotTerminalExpression(AbstractExpression):

	def interpreter(self, context):
		print "非终端解释器",context


class Context(object):

	def __init__(self):
		self.name = ""

if __name__ == "__main__":
	context = Context()
	context.name = 'Andy'
	arr_list = [NotTerminalExpression(),TerminalExpression(),TerminalExpression()]
	for entry in arr_list:
		entry.interpreter(context)
