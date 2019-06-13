from selenium.webdriver.common.by import By
from PO.ManagementCenter import Management_Center
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from Login.login_edu import admin_login
from Login.page import WebPage
import os

class addStudent(Management_Center):
    btn_browse_parent_object_loc = (By.CLASS_NAME, "ke-upload-area")
    btn_browse_loc = (By.TAG_NAME, 'input')
    #添加学生
    def add_student(self):
        # 切换的会员中心页面
        a = self.driver.find_element(By.ID, 'mainframe')
        self.driver.switch_to.frame(a)

        self.driver.find_element(By.LINK_TEXT,'添加学生').click()


    # 输入学生信息
    def ipt_student(self):
        #账号
        self.driver.find_element(By.ID,'username').send_keys('php12345')
        #昵称
        self.driver.find_element(By.ID,'realname').send_keys('大人物')
        #密码
        self.driver.find_element(By.ID,'password').send_keys('123456')
        #性别
        self.driver.find_element(By.XPATH,'//*[@type="radio" and @value ="1"]').click()
        #选择角色
        self.driver.find_element(By.NAME,'roleid').click()
        self.driver.find_element(By.XPATH,'//*[text()="大众会员"]')
        #明星会员
        self.driver.find_element(By.NAME,'isstart').click()
    #上传图片
    def upload_pictures(self):
        self.driver.find_element(By.LINK_TEXT,'上传头像').click()
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div/div[1]/ul/li[2]').click()
        # self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div/div[3]/form/div/div/div/span/input').click()
        # os.system('D:/')
        # self.driver.find_element(By.XPATH,"//*[@value='确定' ]").click()
        ele = self.driver.find_element(By.NAME,'localUrl')
        self.driver.execute_script("arguments[0].removeAttribute('readonly');", ele)
        ele.send_keys('D:/QQ1.png')
        # tpm = self.driver.find_element(*self.btn_browse_parent_object_loc)
        # obj = tpm.find_elements(*self.btn_browse_loc)[1]
        # ActionChains(self.driver).click(obj).perform()
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[3]/span[1]/input')


if __name__=='__main__':
    driver = admin_login()
    run = addStudent(driver)
    run.member()
    run.add_student()
    run.ipt_student()
    run.upload_pictures()