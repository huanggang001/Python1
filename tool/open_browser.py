from selenium import webdriver

# 配置浏览器类型
bs = 'gc'

def create__browser(b=bs):

    if b == 'gc':
        driver = webdriver.Chrome()
    elif b == 'ff':
        driver = webdriver.Firefox()
    elif b == 'ie':
        driver = webdriver.Ie()
    else:
        pass

    return driver


if __name__=='__main__':
    create__browser()





