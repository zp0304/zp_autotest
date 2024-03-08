# coding=UTF-8
import time

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()  # 创建浏览器对象
wd.implicitly_wait(10)
wd.get("http://www.baidu.com")
mainWindow = wd.current_window_handle
search1 = wd.find_element(By.CSS_SELECTOR, "#kw")  # css表达式通过ID定位

news = wd.find_element(By.CSS_SELECTOR, '[href="http://news.baidu.com"]')  # 定位任意元素用[],""和’‘都可以，但此处只能用’‘
news.click()
for handle in wd.window_handles:
    wd.switch_to.window(handle)    # 先切换到该窗口
    if '百度新闻' in wd.title:   #wd.title该窗口的标题栏字符串
        break  # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，

s =wd.find_element(By.ID, 'ww')
s.send_keys("123")
wd.find_element(By.CSS_SELECTOR, '[value="百度一下"]')
wd.switch_to.window(mainWindow)
wd.find_element(By.CSS_SELECTOR, "#kw").send_keys("python")
wd.find_element(By.CSS_SELECTOR, '[value="百度一下"]').click()
wd.find_element(By.CSS_SELECTOR,"#page > div > a:nth-child(2) > span").click()



# ac=ActionChains(wd)  #实例化ActionChains类，以wd作为参数
# ac.move_to_element(wd.find_element(By.CSS_SELECTOR,"#u > a.pf")).perform()  #“perform”执行的意思，必须加上才会移动鼠标