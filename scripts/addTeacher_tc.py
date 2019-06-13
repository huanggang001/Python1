import unittest
from PO.MemberCenter.teacherList import AppendTeacher
from Login.login_edu import admin_login
from PO.ManagementCenter import Management_Center
from tool.my_SQL import ReadMySQLData

class Testloaclhost(unittest.TestCase):
    '''添加教师测试'''
    a = 1
    def setUp(self):

        # 浏览器实例化
        self.driver = admin_login()
        # 添加教师实例化
        self.at = AppendTeacher(self.driver)
        #管理中心实例化
        self.lp =Management_Center(self.driver)

        # 关闭浏览器
    def edu_quit(self):
        self.at.web_close()

    #添加教师
    @unittest.skipIf(a !=1,'')
    def test_addTeacher_1(self):
        '''成功添加教师'''
        ReadMySQLData('delete from xsmart_users where username="1311111111"')
        self.lp.member()
        self.at.add_teacher()
        a = self.at.isteacher(1311111111)
        self.assertEqual(a, '1311111111')

if __name__=='__main__':
    unittest.main()