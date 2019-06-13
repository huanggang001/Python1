from selenium.webdriver.common.by import By
from time import sleep
from Login.page import WebPage


class AppendTeacher(WebPage):

    # 教师列表对象层
    teacher = (By.XPATH, "//*[text()='教师列表']")
    iframe = (By.ID, 'mainframe')
    appedTeacher = (By.LINK_TEXT, '添加教师')
    username1 = (By.ID, 'username')
    realname = (By.NAME, 'realname')
    password1 = (By.NAME, 'password')
    sex = (By.XPATH, '//*[@type="radio" and @value ="1"]')
    selectRoleid = (By.NAME, 'roleid')
    maxPractice = (By.XPATH, '//*[text()="大众会员"]')
    orid = (By.NAME, 'orid1')
    selectOrid = (By.XPATH, "//*[text()='中州大学']")
    email = (By.NAME, 'email')
    phone = (By.NAME, 'phone')
    save = (By.XPATH, "//*[text()='确认保存']")
    retunrList = (By.LINK_TEXT, '返回列表')
    SE = (By.XPATH, '//*[text()="搜索"]')
    titleText = (By.XPATH, "//*[@title='1311111111']")

    # 教师列表操作层
    def practice(self):
        #教师列表
        self.driver.find_element(*self.teacher).click()
        # 切换的会员中心页面
        a = self.driver.find_element(*self.iframe)
        self.driver.switch_to.frame(a)

    def teacherA(self,username,nickname,password,email,phone):
        # 添加教师
        self.driver.find_element(*self.appedTeacher).click()
        # 账号
        self.driver.find_element(*self.username1).send_keys(username)
        # 昵称
        self.driver.find_element(*self.realname).send_keys(nickname)
        # 密码
        self.driver.find_element(*self.password1).send_keys(password)
        # 性别
        self.driver.find_element(*self.sex).click()
        # 选择角色
        self.driver.find_element(*self.selectRoleid).click()
        self.driver.find_element(*self.maxPractice).click()

        # 选择机构
        self.driver.find_element(*self.orid).click()
        self.driver.find_element(*self.selectOrid)
        # 邮箱
        self.driver.find_element(*self.email).send_keys(email)
        # 手机号
        self.driver.find_element(*self.phone).send_keys(phone)
        # 保存
        self.driver.find_element(*self.save).click()
        sleep(3)
        # 警告框
        self.driver.switch_to.alert.accept()
        # 返回列表
        self.driver.find_element(*self.retunrList).click()


    # 判断是否添加成功
    def isteacher(self,phone1):
        # 会员列表搜索
        self.driver.find_element(*self.username1).send_keys(phone1)
        self.driver.find_element(*self.SE).click()
        #返回用户
        b = self.driver.find_element(*self.titleText).text
        return b

    # 教师列表业务层
    def add_teacher(self):
        self.practice()
        self.teacherA(1311111111,'boy','h123456789','hello@163.com',1311111111)

