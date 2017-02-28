#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import unittest

import HTMLTestRunner
import time
import os
import shutil
casepath = ".//TestCase"
#casepath = '/Users/zhaozhiquan/automation/AndroidSdk/TestCase'
def Creatsuite():
    #定义单元测试容器
    testunit = unittest.TestSuite()
    #定搜索用例文件的方法
    discover = unittest.defaultTestLoader.discover(casepath, pattern='test02*', top_level_dir=None)
    #将测试用例加入测试容器中
    for testsuite in discover:
        for casename in testsuite:
            testunit.addTest(casename)
        print testunit
    return testunit
test_case = Creatsuite()
#获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
#定义个报告存放路径，支持相对路径
day = time.strftime('%Y-%m-%d')
aaa=os.path.exists('./result/'+day)
if aaa:
    shutil.rmtree('./result/'+day)
os.mkdir('./result/'+day)
os.mkdir('./result/'+day+'/screencap')
filename = './result/'+day+'/result.html'
fp = file(filename, 'wb')
#定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'iOS联运sdk测试报告', description=u'用例执行情况：')
#运行测试用例
runner.run(test_case)
fp.close()  #关闭报告文件
