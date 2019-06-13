from Login.loginPage import Loginpage


def admin_login(username='admin',password='admin'):
    obj = Loginpage()
    # 登录业务层
    obj.open_url()
    obj.username_page(username)
    obj.password_page(password)
    obj.submit_page()
    return obj.driver

if __name__=='__main__':
    admin_login()