from selenium.webdriver.common.by import By
from Login.page import WebPage

class Management_Center(WebPage):

    # 管理中心对象层
    # 退出登录
    eduquit = (By.XPATH, "/*[text()='退出']")
    # 会员中心
    members = (By.LINK_TEXT, '会员中心')

    # 管理中心操作层

    # 退出登录
    def edu_quit(self):
        # 判断浏览器登录是否成功
        ele = self.driver.find_element(*self.eduquit).text

    # def edu_role(self):
    #     self.driver.find_element(By.XPATH,"/*[@style = 'color:#F00;']").text

    #会员中心
    def member(self):
        self.driver.find_element(*self.members).click()

if __name__=='__main__':
    run = Management_Center()
    run.edu_quit()