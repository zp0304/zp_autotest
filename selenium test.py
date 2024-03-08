# coding=UTF-8
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

wb = webdriver.Chrome()  # 新建浏览器对象
wb.implicitly_wait(10)  # 设置隐式等待（如果找不到元素， 每隔 半秒钟 再去界面上查看一次， 直到找到该元素， 或者 过了10秒 最大时长）
wb.get("http://www.baidu.com")  # 输入url（协议：//域名）
search = wb.find_element(By.ID, "kw")  # 根据ID定位元素
search.send_keys("自动化测试")  # 输入搜索关键词
wb.find_element(By.ID, "su").click()  # 点击“百度一下“--根据ID定位
# 获取输入框里面的文字
print(search.get_attribute('value')) # 获取搜索输入框中的文本
search.clear()  # 清除输入框
search.send_keys("功能测试")  # 输入搜索关键词
wb.find_element(By.ID, "su").click()  # 点击“百度一下“--根据ID定位
# 获取输入框里面的文字
print(search.get_attribute('value')) # 获取搜索输入框中的文本
pic = wb.find_element(By.CLASS_NAME, "s-tab-pic_p4Uej")  # 点击图片----根据class定位（注意：一个元素可能有多个class，选取其中一个否则会报错）
pic.click()

# 根据Tag定位，一般很多元素tag一致
# 如果用elements，则返回当前页面所有符合tag名的对象，放在列表中
# 如果用element，则返回当前页面第一个符合tag名的对象
tag1 = wb.find_elements(By.TAG_NAME, "div")
for element in tag1:
    print(element.text)  # 取出列表中的每个 WebElement对象，打印出其text属性的值
print(wb.find_element(By.TAG_NAME, "div").text)


# 通过WebElement对象选择元素(先定位到网页中的某个对象，再定位到该对象内部)
wbelement = wb.find_element(By.ID, "bdpcImgTab")  # 先定位到网页中的某个对象
print(wbelement.find_element(By.CLASS_NAME, "s_tab_ps").text)  # 1、定位到该对象内部 2、.text获取class为"s_tab_ps"元素的文本内容

# 获取元素属性的值，就可以使用 element.get_attribute('属性')
print(wbelement.get_attribute("class"))  # s_tab
print(wbelement.get_attribute("id"))  # bdpcImgTab

# 获取整个元素对应的HTML
# 要获取整个元素对应的HTML文本内容，可以使用 element.get_attribute('outerHTML')
# 如果，只是想获取某个元素 内部 的HTML文本内容，可以使用 element.get_attribute('innerHTML')
print(wbelement.get_attribute('outerHTML'))
print(wbelement.get_attribute('innerHTML'))


print(wbelement.get_attribute('innerText')) # 显示元素可见文本内容
print(wbelement.get_attribute('textContent')) # 显示所有内容（包括display属性为none的部分）


