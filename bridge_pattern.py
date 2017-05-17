#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
大话设计模式
设计模式——桥接模式
桥接模式(Bridge Pattern):将抽象部分与它的实现部分分离，使它们都可以独立地变化.
"""

# 抽象手机软件类
class HandsetSoft(object):

	def run(self):
		pass

#具体游戏类,游戏是手机软件,继承抽象手机软件类
class HandsetGame(HandsetSoft):

	def run(self):
		print "运行手机游戏"

#手机通讯录
class  HandsetAddressList(HandsetSoft):

	def run(self):
		print "运行通信录"


#抽象手机品牌类
class HandsetBrand(object):

	def __init__(self):
		self.soft = ""

	def set_handsetsoft(self,soft):
		self.soft = soft

	def run(self):
		pass

# 手机品牌N
class HandsetBrandN(HandsetBrand):

	def run(self):
		self.soft.run()

# 手机品牌M
class HandsetBrandM(HandsetBrand):

	def run(self):
		self.soft.run()

if __name__ == "__main__":
	game = HandsetGame()
	address = HandsetAddressList()

	phoneN = HandsetBrandN()
	phoneN.set_handsetsoft(game)
	phoneN.run()

	phoneM = HandsetBrandM()
	phoneM.set_handsetsoft(address)
	phoneM.run()
