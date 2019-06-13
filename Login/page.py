from tool.open_browser import create__browser

sit_url = 'http://localhost/admin.php'

# 启动浏览器

class WebPage(object):

    def __init__(self,driver=''):

        b =driver
        if b =='':
            self.driver = create__browser()
        else:
            self.driver = b

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def open_url(self,url =sit_url):
        self.driver.get(url)

    def web_close(self):
        self.driver.quit()



if __name__=='__main__':
    run = WebPage()
    run.open_url()
