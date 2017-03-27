# coding=utf-8
import unittest
import os
from time import sleep
from appium import webdriver
import public.methods as t
import public.case_xls as xl
class IOSSDK(unittest.TestCase,t.Methods,xl.Case_xls):
	u'''用户协议,手机号注册'''
	def setUp(self):
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps())
		self.case_id = self.get_col(1,0)  # case id 列
		self.preset = self.get_col(1,2)  # 预置条件列
		self.using = self.get_col(1,5)  # 查找元素方式列
		self.value = self.get_col(1,6)  # 元素列
		self.exp = self.get_col(1,7)  # 预期结果列
		self.driver.implicitly_wait(10)
	def tearDown(self):
		self.driver.quit()

	def test_101(self):
		u'''查看用户协议'''
		try:
			self.element(self.driver,'name','显示登录UI').click()
		except:pass
		self.element(self.driver, 'name', 'Done').click()  # 隐藏键盘
		self.element(self.driver,self.using[1], self.value[1]).click()  #进入用户协议
		el = self.element(self.driver,self.using[2], self.value[2])     #协议title
		print unicode('测试结果: %s' %el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[1].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.text), self.exp[1], self.case_id[1])  # 断言
	def test_102(self):
		u'''查看用户协议,返回'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver, 'name', 'Done').click()  # 隐藏键盘
		self.element(self.driver,self.using[3], self.value[3]).click()  # 进入用户协议
		self.element(self.driver,self.using[4], self.value[4]).click()  #返回
		sleep(2)
		el = self.element(self.driver,self.using[5], self.value[5])     #游客登录按钮
		print unicode('测试结果: %s' % el.get_attribute('name').encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[3].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.get_attribute('name')), self.exp[3], self.case_id[3])  # 断言

	def test_103(self):
		u'''手机号注册，输入为空'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[6], self.value[6]).click()   #新用户注册
		for i in xrange(10):
			self.element(self.driver,self.using[7], self.value[7]).click()   #获取验证码

			el = self.element(self.driver,self.using[8], self.value[8])      #提示
			if el.text !=None:
				break
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[6].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.text), self.exp[6], self.case_id[6])  # 断言

	def test_104(self):
		u'''手机号注册，输入10位数字'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[9], self.value[9]).click()   #新用户注册
		for i in range(10):
			el = self.element(self.driver,self.using[10], self.value[10])  # 手机号输入框

			el.send_keys(self.preset[10].encode('utf-8').decode("utf-8")) #输入
			sleep(2)
			el2 = self.element(self.driver,self.using[10], '//*[@value=%s]'% self.preset[10]) #重新获取该元素
			if el2.text == self.preset[10]:  #判断输入的与 预置是否一致
				break
		for i in xrange(10):
			self.element(self.driver,self.using[11], self.value[11]).click()    #获取验证码

			el3 = self.element(self.driver,self.using[12], self.value[12])     #提示
			if el3.text != None:
				break
		print unicode('测试结果: %s' % el3.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[9].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el3.text), self.exp[9], self.case_id[9])  # 断言

	def test_105(self):
		u'''手机号注册，输入12位数字'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[13], self.value[13]).click()   #新用户注册
		for i in range(10):
			el = self.element(self.driver,self.using[14], self.value[14])  # 手机号输入框

			el.send_keys(self.preset[14].encode('utf-8').decode("utf-8")) #输入
			sleep(2)
			el2 = self.element(self.driver,self.using[14], '//*[@value=%s]'% self.preset[14]) #重新获取该元素
			if el2.text == self.preset[14]:  #判断输入的与 预置是否一致
				break
		for i in xrange(10):
			self.element(self.driver,self.using[15], self.value[15]).click()    #获取验证码

			el3 = self.element(self.driver,self.using[16], self.value[16])     #提示
			if el3.text != None:
				break
		print unicode('测试结果: %s' % el3.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[13].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el3.text), self.exp[13], self.case_id[13])  # 断言

	def test_106(self):
		u'''手机号注册，输入11位数字'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[17], self.value[17]).click()   #新用户注册
		for i in range(10):
			el = self.element(self.driver,self.using[18], self.value[18])  # 手机号输入框

			el.send_keys(self.preset[18].encode('utf-8').decode("utf-8")) #输入
			sleep(2)
			el2 = self.element(self.driver,self.using[18], '//*[@value=%s]'% self.preset[18]) #重新获取该元素
			if el2.text == self.preset[18]:  #判断输入的与 预置是否一致
				break
		self.element(self.driver,self.using[19], self.value[19]).click()    #获取验证码

		el3 = self.element(self.driver,self.using[20], self.value[20])     #提示
		try:
			print ('测试结果: %s' % el3.text.encode('utf-8'))
			print ('预期结果: %s' % self.exp[17].encode('utf-8'))
			self.dy_Equal(self.driver, unicode(el3.text), self.exp[17], self.case_id[17])  # 断言
		except:
			print ('测试结果: %s' % el3)
			print ('预期结果: 元素不为空')
			self.dy_IsNotNone(self.driver,el3,self.case_id[17])

	def test_107(self):
		u'''手机号注册，正确手机号，验证码为空'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[21], self.value[21]).click()   #新用户注册
		for i in range(10):
			el = self.element(self.driver,self.using[22], self.value[22])  # 手机号输入框
			el.send_keys(self.preset[22].encode('utf-8').decode("utf-8")) #输入
			el2 = self.element(self.driver,self.using[22], '//*[@value=%s]'% self.preset[22]) #重新获取该元素
			if el2.text == self.preset[22]:  #判断输入的与 预置是否一致
				break
		for i in xrange(10):
			self.element(self.driver,self.using[23], self.value[23]).click()    #下一步
			el3 = self.element(self.driver,self.using[24], self.value[24])     #提示
			if el3.text !=None:
				break
		print unicode('测试结果: %s' % el3.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[21].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el3.text), self.exp[21], self.case_id[21])  # 断言

	def test_108(self):
		u'''手机号注册，正确手机号，错误验证码'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[25], self.value[25]).click()   #新用户注册
		for i in range(10):
			el = self.element(self.driver,self.using[26], self.value[26])  # 手机号输入框
			el.send_keys(self.preset[26].encode('utf-8').decode("utf-8")) #输入
			el2 = self.element(self.driver,self.using[26], '//*[@value=%s]'% self.preset[26]) #重新获取该元素
			if el2.text == self.preset[26]:  #判断输入的与 预置是否一致
				break
		el4 = self.element(self.driver,self.using[27], self.value[27])     #输入验证码
		el4.send_keys(self.preset[27].encode('utf-8').decode("utf-8"))
		for i in xrange(10):
			self.element(self.driver,self.using[28], self.value[28]).click()    #下一步
			el3 = self.element(self.driver,self.using[29], self.value[29])     #提示
			if el3.text != None:
				break
		print unicode('测试结果: %s' % el3.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[25].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el3.text), self.exp[25], self.case_id[25])  # 断言

	def test_109(self):
		u'''手机号注册，正确手机号，过期验证码'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[30], self.value[30]).click()   #新用户注册
		for i in range(10):
			el = self.element(self.driver,self.using[31], self.value[31])  # 手机号输入框
			el.send_keys(self.preset[31].encode('utf-8').decode("utf-8")) #输入
			el2 = self.element(self.driver,self.using[31], '//*[@value=%s]'% self.preset[31]) #重新获取该元素
			if el2.text == self.preset[31]:  #判断输入的与 预置是否一致
				break
		el4 = self.element(self.driver,self.using[32], self.value[32])     #输入验证码
		el4.send_keys(self.preset[32].encode('utf-8').decode("utf-8"))
		for i in xrange(10):
			self.element(self.driver,self.using[33], self.value[33]).click()    #下一步
			el3 = self.element(self.driver,self.using[34], self.value[34])     #提示
			if el3.text != None:
				break
		print unicode('测试结果: %s' % el3.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[30].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el3.text), self.exp[30], self.case_id[30])  # 断言

	def yanzhengma(self):
		'''
		#手机注册输入验证码
		:return:
		'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[35], self.value[35]).click()   #新用户注册
		for i in range(10):
			el = self.element(self.driver,self.using[36], self.value[36])  # 手机号输入框
			el.send_keys(self.preset[36].encode('utf-8').decode("utf-8")) #输入
			el2 = self.element(self.driver,self.using[36], '//*[@value=%s]'% self.preset[36]) #重新获取该元素
			if el2.text == self.preset[36]:  #判断输入的与 预置是否一致
				break
		el4 = self.element(self.driver,self.using[37], self.value[37])     #输入验证码
		el4.send_keys(self.preset[37].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[38], self.value[38]).click()    #下一步
		sleep(2)
	def test_110(self):
		u'''手机号注册，正确手机号，正确验证码'''
		self.yanzhengma()
		el = self.element(self.driver,self.using[39], self.value[39])     #提示
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[35].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.text), self.exp[35], self.case_id[35])  # 断言

	def test_111(self):
		u'''手机号注册，密码与确认密码为空'''
		self.yanzhengma()                       #40
		for i in xrange(10):
			self.element(self.driver,self.using[41], self.value[41]).click()  #提交
			el = self.element(self.driver,self.using[42], self.value[42])     #提示
			if el.text != None:
				break
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[40].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.text), self.exp[40], self.case_id[40])  # 断言

	def test_112(self):
		u'''手机号注册，密码与确认少于6位'''
		self.yanzhengma()                       #43
		el1 = self.element(self.driver,self.using[44], self.value[44])     #密码输入框
		el1.send_keys(self.preset[44].encode('utf-8').decode("utf-8"))
		el2 = self.element(self.driver,self.using[45], self.value[45])  # 确认密码密码输入框
		el2.send_keys(self.preset[45].encode('utf-8').decode("utf-8"))
		for i in xrange(10):
			self.element(self.driver,self.using[46], self.value[46]).click()  #提交
			el = self.element(self.driver,self.using[47], self.value[47])     #提示
			if el.text != None:
				break
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[43].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.text), self.exp[43], self.case_id[43])  # 断言

	def test_113(self):
		u'''手机号注册，密码与确认不一致'''
		self.yanzhengma()                       #48
		el1 = self.element(self.driver,self.using[49], self.value[49])     #密码输入框
		el1.send_keys(self.preset[49].encode('utf-8').decode("utf-8"))
		el2 = self.element(self.driver,self.using[50], self.value[50])  # 确认密码密码输入框
		el2.send_keys(self.preset[50].encode('utf-8').decode("utf-8"))
		for i in xrange(10):
			self.element(self.driver,self.using[51], self.value[51]).click()  #提交
			el = self.element(self.driver,self.using[52], self.value[52])     #提示
			if el.text != None:
				break
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[48].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.text), self.exp[48], self.case_id[48])  # 断言

	def test_114(self):
		u'''手机号注册，密码与确认一致'''
		self.yanzhengma()                       #53
		el1 = self.element(self.driver,self.using[54], self.value[54])     #密码输入框
		el1.send_keys(self.preset[54].encode('utf-8').decode("utf-8"))
		el2 = self.element(self.driver,self.using[55], self.value[55])  # 确认密码密码输入框
		el2.send_keys(self.preset[55].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[56], self.value[56]).click()  #提交
		sleep(5)
		el = self.element(self.driver,self.using[57], self.value[57])     #提示
		print ('测试结果: %s' % el.get_attribute('name').encode('utf-8'))
		print ('预期结果: %s' % self.exp[53].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.get_attribute('name')), self.exp[53], self.case_id[53])  # 断言

	def test_115(self):
		u'''手机号注册，返回'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		el = self.element(self.driver,'name','游客登录')
		el.get_attribute('name')
		self.element(self.driver,self.using[58], self.value[58]).click()   #新用户注册
		self.element(self.driver,self.using[59], self.value[59]).click()   #返回
		el = self.element(self.driver,self.using[60], self.value[60])      #登录按钮
		print ('测试结果: %s' % el.get_attribute('name').encode('utf-8'))
		print ('预期结果: %s' % self.exp[58].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.get_attribute('name')), self.exp[58], self.case_id[58])  # 断言



