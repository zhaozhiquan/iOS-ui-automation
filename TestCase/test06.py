# coding=utf-8
import unittest
import os
import random
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import public.methods as t
import public.case_xls as xl
class IOSSDK(unittest.TestCase,t.Methods,xl.Case_xls):
	u'''第三方登录'''
	def setUp(self):
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps())
		self.case_id = self.get_col(6,0)  # case id 列
		self.preset = self.get_col(6,2)  # 预置条件列
		self.using = self.get_col(6,5)  # 查找元素方式列
		self.value = self.get_col(6,6)  # 元素列
		self.exp = self.get_col(6,7)  # 预期结果列
		self.driver.implicitly_wait(10)
	def tearDown(self):
		self.driver.quit()

	def test_601(self):
		u'''自动登录'''
		self.element(self.driver, self.using[1], self.value[1]).click()   #勾选自动登录按钮
		self.element(self.driver,self.using[2],self.value[2]).click()     #关闭按钮
		sleep(2)
		self.tap(self.driver,(self.using[3],self.value[3]))               #公告的确定按钮
		sleep(2)
		self.tap(self.driver, (self.using[4], self.value[4]))             #点击用户中心接口
		el = self.element_or_none(self.driver, self.using[5], self.value[5]) #登录按钮
		print unicode('测试结果: %s' % el.get_attribute('name').encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[1].encode('utf-8'))
		self.dy_Equal(self.driver,unicode(el.get_attribute('name')),self.exp[1],self.case_id[1])
		sleep(5)
		el2 = self.element_or_none(self.driver,self.using[5],self.value[5])   #登录按钮
		#如果el2 为空,则正常,断言成功,如果el2不为空,则自动登录失败,断言失败
		print unicode('测试结果: %s' % el2)
		print unicode('预期结果: 元素为空')
		self.dy_IsNone(self.driver, el2, self.case_id[1])

	def zhongxin(self):
		sleep(5)
		try:
			self.element_or_none(self.driver, self.using[5], self.value[5]).click()  #登录按钮
		except:pass
		for i in xrange(10):

			self.tap(self.driver, (self.using[3], self.value[3]))  # 公告的确定按钮
			sleep(2)
			self.tap(self.driver, (self.using[4], self.value[4]))  #用户中心按钮
			try:
				el =self.element(self.driver,self.using[9],self.value[9])
				if el.get_attribute('name').encode('utf-8') == '切换账号':
					break
			except:pass
		sleep(2)
	def test_602(self):
		u'''用户中心界面，点击右上角的X按钮'''
		self.zhongxin()
		self.element(self.driver, self.using[8], self.value[8]).click()    #X按钮
		sleep(2)
		el2 = self.element_or_none(self.driver,self.using[9],self.value[9])
		print unicode('测试结果: %s' % el2)
		print unicode('预期结果: 元素为空')
		self.dy_IsNone(self.driver, el2, self.case_id[6])
	def test_603(self):
		u'''进入解绑与绑定，返回'''
		self.zhongxin()
		self.element(self.driver, self.using[10], self.value[10]).click()  #解绑与绑定手机
		self.element(self.driver, self.using[11], self.value[11]).click()  #返回
		el = self.element_or_none(self.driver,self.using[12], self.value[12])
		print unicode('测试结果: %s' % el)
		print unicode('预期结果: 元素为空')
		self.dy_IsNone(self.driver, el, self.case_id[10])

	def test_604(self):
		u'''解绑手机，手机号输入框，清除'''
		self.zhongxin()
		self.element(self.driver, self.using[13], self.value[13]).click()  #解绑与绑定手机
		self.element(self.driver, self.using[14], self.value[14]).clear()  # 手机号输入框
		el = self.element_or_none(self.driver,self.using[15], self.value[15])  #查看输入框是否被清除
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[13].encode('utf-8'))
		self.dy_Equal(self.driver,unicode(el.text),self.exp[13],self.case_id[13])

	def test_605(self):
		u'''解绑手机，点击获取验证码'''
		self.zhongxin()
		self.element(self.driver, self.using[16], self.value[16]).click()  #解绑与绑定手机
		self.element(self.driver, self.using[17], self.value[17]).click()  # 点击获取验证码
		el = self.element(self.driver, self.using[18], self.value[18])  # 提示
		try:
			print unicode('测试结果: %s' % el.text.encode('utf-8'))
			print unicode('预期结果: %s' % self.exp[16].encode('utf-8'))
			self.dy_Equal(self.driver, unicode(el.text), self.exp[16], self.case_id[16])  # 断言
		except:
			print unicode('测试结果: %s' % el)
			print unicode('预期结果: 元素不为空')
			self.dy_IsNotNone(self.driver, el, self.case_id[16])

	def test_606(self):
		u'''解绑手机号，验证输入为空'''
		self.zhongxin()
		self.element(self.driver, self.using[19], self.value[19]).click()  #解绑与绑定手机
		for i in xrange(10):
			self.element(self.driver,self.using[20], self.value[20]).click()    #解绑
			el3 = self.element(self.driver,self.using[21], self.value[21])     #提示
			if el3.text !=None:
				break
		print unicode('测试结果: %s' % el3.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[19].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el3.text), self.exp[19], self.case_id[19])  # 断言

	def test_607(self):
		u'''解绑手机号，输入错误验证码'''
		self.zhongxin()
		self.element(self.driver, self.using[22], self.value[22]).click()  #解绑与绑定手机
		el = self.element(self.driver, self.using[23], self.value[23])     #验证码输入框
		el.send_keys(self.preset[23].encode('utf-8').decode("utf-8"))
		for i in xrange(10):
			self.element(self.driver,self.using[24], self.value[24]).click()    #解绑
			el3 = self.element(self.driver,self.using[25], self.value[25])     #提示
			if el3.text !=None:
				break
		print unicode('测试结果: %s' % el3.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[22].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el3.text), self.exp[22], self.case_id[22])  # 断言

	def test_608(self):
		u'''解绑手机号，输入正确验证码'''
		self.zhongxin()
		self.element(self.driver, self.using[26], self.value[26]).click()  #解绑与绑定手机
		el = self.element(self.driver, self.using[27], self.value[27])      #验证码输入框
		el.send_keys(self.preset[27].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[28], self.value[28]).click()    #解绑
		el3 = self.element(self.driver,self.using[29], self.value[29])     #提示
		print unicode('测试结果: %s' % el3.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[26].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el3.text), self.exp[26], self.case_id[26])  # 断言

	def test_609(self):
		u'''绑定手机号，手机号输入为空'''
		self.zhongxin()
		self.element(self.driver, self.using[30], self.value[30]).click()  #解绑与绑定手机
		for i in xrange(10):
			self.element(self.driver,self.using[31], self.value[31]).click()    #获取验证码
			el3 = self.element(self.driver,self.using[32], self.value[32])     #提示
			if el3.text !=None:
				break
			sleep(2)
		print unicode('测试结果: %s' % el3.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[30].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el3.text), self.exp[30], self.case_id[30])  # 断言

	def test_610(self):
		u'''绑定手机号，手机号输入10位数'''
		self.zhongxin()
		self.element(self.driver, self.using[33], self.value[33]).click()  #解绑与绑定手机
		for i in range(10):
			el = self.element(self.driver,self.using[34], self.value[34])  # 手机号输入框
			el.send_keys(self.preset[34].encode('utf-8').decode("utf-8")) #输入
			el2 = self.element(self.driver,self.using[34], '//*[@value=%s]'% self.preset[34]) #重新获取该元素
			if el2.text == self.preset[34]:  #判断输入的与 预置是否一致
				break
			else:
				el.clear()
		for i in xrange(10):
			self.element(self.driver,self.using[35], self.value[35]).click()    #获取验证码
			el3 = self.element(self.driver,self.using[36], self.value[36])     #提示
			if el3.text !=None:
				break
			sleep(2)
		print unicode('测试结果: %s' % el3.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[33].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el3.text), self.exp[33], self.case_id[33])  # 断言

	def test_611(self):
		u'''绑定手机号，手机号输入12位数'''
		self.zhongxin()
		self.element(self.driver, self.using[37], self.value[37]).click()  #解绑与绑定手机
		for i in range(10):
			el = self.element(self.driver,self.using[38], self.value[38])  # 手机号输入框
			el.send_keys(self.preset[38].encode('utf-8').decode("utf-8")) #输入
			el2 = self.element(self.driver,self.using[38], '//*[@value=%s]'% self.preset[38]) #重新获取该元素
			if el2.text == self.preset[38]:  #判断输入的与 预置是否一致
				break
			else:
				el.clear()
		for i in xrange(10):
			self.element(self.driver,self.using[39], self.value[39]).click()    #获取验证码
			el3 = self.element(self.driver,self.using[40], self.value[40])     #提示
			if el3.text !=None:
				break
			sleep(2)
		print unicode('测试结果: %s' % el3.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[37].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el3.text), self.exp[37], self.case_id[37])  # 断言

	def test_612(self):
		u'''绑定手机号，手机号输入11位数'''
		self.zhongxin()
		self.element(self.driver, self.using[41], self.value[41]).click()  #解绑与绑定手机
		for i in range(10):
			el = self.element(self.driver,self.using[42], self.value[42])  # 手机号输入框
			el.send_keys(self.preset[42].encode('utf-8').decode("utf-8")) #输入
			el2 = self.element(self.driver,self.using[42], '//*[@value=%s]'% self.preset[42]) #重新获取该元素
			if el2.text == self.preset[42]:  #判断输入的与 预置是否一致
				break
			else:
				el.clear()
		self.element(self.driver, self.using[43], self.value[43]).click()  #获取验证码
		el3 = self.element(self.driver, self.using[44], self.value[44])  # 提示
		try:
			print unicode('测试结果: %s' % el3.text.encode('utf-8'))
			print unicode('预期结果: %s' % self.exp[41].encode('utf-8'))
			self.dy_Equal(self.driver, unicode(el3.text), self.exp[41], self.case_id[41])  # 断言
		except:
			print unicode('测试结果: %s' % el3)
			print unicode('预期结果: 元素不为空')
			self.dy_IsNotNone(self.driver, el3, self.case_id[41])

	def test_613(self):
		u'''绑定手机号，正确手机号，验证码为空'''
		self.zhongxin()
		self.element(self.driver, self.using[45], self.value[45]).click()  #解绑与绑定手机
		for i in range(10):
			el = self.element(self.driver,self.using[46], self.value[46])  # 手机号输入框
			el.send_keys(self.preset[46].encode('utf-8').decode("utf-8")) #输入
			el2 = self.element(self.driver,self.using[46], '//*[@value=%s]'% self.preset[46]) #重新获取该元素
			if el2.text == self.preset[46]:  #判断输入的与 预置是否一致
				break
			else:
				el.clear()
		for i in xrange(10):
			self.element(self.driver,self.using[47], self.value[47]).click()    #绑定
			el3 = self.element(self.driver,self.using[48], self.value[48])     #提示
			if el3.text !=None:
				break
			sleep(2)
		print unicode('测试结果: %s' % el3.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[45].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el3.text), self.exp[45], self.case_id[45])  # 断言

	def test_614(self):
		u'''绑定手机号，正确手机号，过期验证码'''
		self.zhongxin()
		self.element(self.driver, self.using[49], self.value[49]).click()  #解绑与绑定手机
		for i in range(10):
			el = self.element(self.driver,self.using[50], self.value[50])  # 手机号输入框
			el.send_keys(self.preset[50].encode('utf-8').decode("utf-8")) #输入
			el2 = self.element(self.driver,self.using[50], '//*[@value=%s]'% self.preset[50]) #重新获取该元素
			if el2.text == self.preset[50]:  #判断输入的与 预置是否一致
				break
			else:
				el.clear()
		el4 = self.element(self.driver,self.using[51], self.value[51])        #验证码输入框
		el4.send_keys(self.preset[51].encode('utf-8').decode("utf-8"))       # 输入
		for i in xrange(10):
			self.element(self.driver,self.using[52], self.value[52]).click()    #绑定
			el3 = self.element(self.driver,self.using[53], self.value[53])     #提示
			if el3.text !=None:
				break
			sleep(2)
		print unicode('测试结果: %s' % el3.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[49].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el3.text), self.exp[49], self.case_id[49])  # 断言

	def test_615(self):
		u'''绑定手机号，正确手机号，错误验证码'''
		self.zhongxin()
		self.element(self.driver, self.using[54], self.value[54]).click()  #解绑与绑定手机
		for i in range(10):
			el = self.element(self.driver,self.using[55], self.value[55])  # 手机号输入框
			el.send_keys(self.preset[55].encode('utf-8').decode("utf-8")) #输入
			el2 = self.element(self.driver,self.using[55], '//*[@value=%s]'% self.preset[55]) #重新获取该元素
			if el2.text == self.preset[55]:  #判断输入的与 预置是否一致
				break
			else:
				el.clear()
		el4 = self.element(self.driver,self.using[56], self.value[56])        #验证码输入框
		el4.send_keys(self.preset[56].encode('utf-8').decode("utf-8"))       # 输入
		for i in xrange(10):
			self.element(self.driver,self.using[57], self.value[57]).click()    #绑定
			el3 = self.element(self.driver,self.using[58], self.value[58])     #提示
			if el3.text !=None:
				break
			sleep(2)
		print unicode('测试结果: %s' % el3.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[54].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el3.text), self.exp[54], self.case_id[54])  # 断言

	def test_616(self):
		u'''绑定手机号，正确手机号，正确验证码'''
		self.zhongxin()
		self.element(self.driver, self.using[59], self.value[59]).click()  #解绑与绑定手机
		for i in range(10):
			el = self.element(self.driver,self.using[60], self.value[60])  # 手机号输入框
			el.send_keys(self.preset[60].encode('utf-8').decode("utf-8")) #输入
			el2 = self.element(self.driver,self.using[60], '//*[@value=%s]'% self.preset[60]) #重新获取该元素
			if el2.text == self.preset[60]:  #判断输入的与 预置是否一致
				break
			else:
				el.clear()
		el4 = self.element(self.driver,self.using[61], self.value[61])        #验证码输入框
		el4.send_keys(self.preset[61].encode('utf-8').decode("utf-8"))       # 输入
		self.element(self.driver,self.using[62], self.value[62]).click()    #绑定
		el3 = self.element(self.driver,self.using[63], self.value[63])     #提示
		print unicode('测试结果: %s' % el3.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[59].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el3.text), self.exp[59], self.case_id[59])  # 断言

	def test_617(self):
		u'''切换账号'''
		self.zhongxin()
		self.element(self.driver, self.using[64], self.value[64]).click()  #切换账号
		el = self.element(self.driver, self.using[65], self.value[65])  #查找登录按钮
		print unicode('测试结果: %s' % el.get_attribute('name').encode('utf-8'))
		print unicode('预期结果: %s'% self.exp[64].encode('utf-8'))
		self.dy_Equal(self.driver,unicode(el.get_attribute('name')),self.exp[64],self.case_id[64])

	def test_618(self):
		u'''未登录，点击用户中心'''
		self.element(self.driver, self.using[66], self.value[66]).click()  #X按钮
		sleep(2)
		self.tap(self.driver, (self.using[3], self.value[3]))  # 公告的确定按钮
		sleep(2)
		self.tap(self.driver, (self.using[4], self.value[4]))  # 点击用户中心接口
		el = self.element(self.driver, self.using[69], self.value[69])   #登录按钮
		print unicode('测试结果: %s' % el.get_attribute('name').encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[66].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.get_attribute('name')), self.exp[66], self.case_id[66])  # 断言
		try:
			self.test_608()
		except:
			print unicode('解绑出错,请自行解绑:17912345678')


