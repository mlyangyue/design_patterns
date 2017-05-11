#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'

'''
大话设计模式
用任意一种面向对象语言实现一个计算器控制台程序。要求输入两个数和运算符号，得到结果
设计模式——简单工厂模式
简单工厂模式(Simple Factory Pattern):是通过专门定义一个类来负责创建其他类的实例，被创建的实例通常都具有共同的父类。
'''

class Operation(object):
	'''

	四则运算的父类,接收用户输入的数值
	'''
	def __init__(self, number1=0, number2=0):
		self.num1 = number1
		self.num2 = number2

	def GetResult(self):
		pass
	pass

#加法运算类
class OperationAdd(Operation):
	def GetResult(self):
		return self.num1 + self.num2

#减法运算类
class OperationSub(Operation):
	def GetResult(self):
		return self.num1 - self.num2

#乘法运算类
class OperationMul(Operation):
	def GetResult(self):
		return self.num1 * self.num2

#除法运算类
class OperationDiv(Operation):
	def GetResult(self):
		if self.num2 == 0:
			return '除数不能为0 '
		return 1.0*self.num1 / self.num2

#其他操作符类
class OperationUndef(Operation):
	def GetResult(self):
		return '操作符错误'

#简单工厂类
class OperationFactory(object):
	def choose_oper(self,ch):
		if ch == '+':
			return OperationAdd()
		elif ch == '-':
			return OperationSub()
		elif ch == '*':
			return OperationMul()
		elif ch == '/':
			return OperationDiv()
		else:
			return OperationUndef()

if __name__ == "__main__":
	ch = ''
	while not ch == 'q':
		num1 = input('请输入第一个数值:  ')
		oper = str(raw_input('请输入一个四则运算符:  '))
		num2 = input('请输入第二个数值:  ')
		# Operation(num1,num2)
		OF = OperationFactory()
		oper_obj = OF.choose_oper(oper)
		oper_obj.num1 = num1
		oper_obj.num2 = num2
		print '运算结果为: ',oper_obj.GetResult()
