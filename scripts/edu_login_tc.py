import unittest
import sys
from Login.loginPage import Loginpage
from tool.edu_openpyxl import login_requirename,case_local,getTestData
import time


class EduLogin(unittest.TestCase):
    '''系统登录测试'''
    a = 1
    def setUp(self):
        self.obj = Loginpage()
        self.obj.open_url()

    def tearDown(self):
        self.obj.web_close()

    @unittest.skipIf(a !=11,'')
    def test_login_1(self):
        '''登录成功'''
        casename = sys._getframe().f_code.co_name
        data = getTestData(case_local,login_requirename,casename)
        self.obj.login(data[0],data[1])
        a = self.obj.edu_role()
        self.assertEqual(a, data[1])

    @unittest.skipIf(a != 1, '')
    def test_login_2(self):
        '''账号为空测试'''
        casename = sys._getframe().f_code.co_name
        data = getTestData(case_local,login_requirename,casename)
        self.obj.login(data[0],data[1])
        a = self.obj.edu_username_None()
        self.assertEqual(a,'帐号或密码不能为空')
        # a = self.obj.edu_password_error()
        # self.assertEqual(a, '密码错误')

    @unittest.skipIf(a != 11, '')
    def test_login_3(self):
        '''密码为空测试'''
        casename =sys._getframe().f_code.co_name
        data = getTestData(case_local,login_requirename,casename)
        self.obj.login(data[0],data[1])
        # a = self.obj.edu_username_None()
        # self.assertEqual(a, '帐号或密码不能为空')
        a = self.obj.edu_password_error()
        self.assertEqual(a, '密码错误')

    @unittest.skipIf(a != 11, '')
    def test_login_4(self):
        '''登录账号错误'''
        casename = sys._getframe().f_code.co_name
        data = getTestData(case_local,login_requirename,casename)
        self.obj.login(data[0],data[1])
        a = self.obj.edu_password_error()
        self.assertEqual(a,'密码错误')

    @unittest.skipIf(a != 11, '')
    def test_login_5(self):
        '''登录密码错误'''
        casename =sys._getframe().f_code.co_name
        data =getTestData(case_local,login_requirename,casename)
        self.obj.login(data[0],data[1])
        a = self.obj.edu_password_error()
        self.assertEqual(a, '密码错误')




if __name__=='__main__':
    unittest.main()