#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
大话设计模式
设计模式——外观模式
facade_pattern.py
外观模式(Facade Pattern):为子系统中的一组接口提供一个一致界面,此模式定义一个高层接口,使得子系统更加容易是用
"""
# 外观类
class Fund(object):

	def __init__(self):
		self.stocka = StockA()
		self.stockb = StockB()
		self.realty = Realty()

	def buy(self):
		self.stocka.buy()
		self.stockb.buy()
		self.realty.buy()

	def sell(self):
		self.stocka.sell()
		self.stockb.sell()
		self.realty.sell()

# 投资股票A类
class StockA(object):

	def buy(self):
		print 'buy StockA'

	def sell(self):
		print 'sell StockA'
# 投资股票B类
class StockB(object):

	def buy(self):
		print 'buy StockB'

	def sell(self):
		print 'sell StockB'

# 投资房地产
class Realty(object):

	def buy(self):
		print 'buy Realty'

	def sell(self):
		print 'sell Realty'



if __name__=="__main__":

	fund = Fund()
	fund.buy()
	fund.sell()


