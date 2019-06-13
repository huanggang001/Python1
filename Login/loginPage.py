from selenium.webdriver.common.by import By
from Login.page import WebPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#  登录模块
class Loginpage(WebPage):

    # 登录模块对象层
    # 账号
    username = (By.ID, 'username')
    # 密码
    password = (By.NAME, 'password')
    # 提交
    submit = (By.CLASS_NAME, 'admin-btn')
    #判断登录成功
    succeed = (By.XPATH,'//*[@id="header"]/p/span[1]/strong')
    # 判断账号不能为空
    edu_username = (By.ID,'username_msg')
    #判断输入账号/密码错误
    edu_password = (By.ID,'password_msg')

     #登录模块操作层
    def username_page(self,username):
        self.driver.find_element(*self.username).send_keys(username)

    def password_page(self,password):
        self.driver.find_element(*self.password).send_keys(password)

    def submit_page(self):
        self.driver.find_element(*self.submit).click()

    #判断登录成功
    def edu_role(self):
        a =self.driver.find_element(*self.succeed).text
        return a
    #判断登录账号不能为空
    def edu_username_None(self):
        WebDriverWait(self.driver,10,0.5).until(EC.text_to_be_present_in_element(self.edu_username,u"帐号或密码不能为空"))
        a = self.driver.find_element(*self.edu_username).text
        return a

    # #判断输入账号/密码错误
    def edu_password_error(self):
        WebDriverWait(self.driver, 10 ,0.5).until(EC.text_to_be_present_in_element(self.edu_password,"密码错误"))
        a = self.driver.find_element(*self.edu_password).text
        return a





    # 业务层
    def login(self,username,password):
        self.username_page(username)
        self.password_page(password)
        self.submit_page()




if __name__=='__main__':
    run = Loginpage()
    run.open_url()
    run.login()
