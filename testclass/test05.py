# WebDriver常用方法
# 点击和输入
# 前面我们已经学习了定位元素， 定位只是第一步， 定位之后需要对这个元素进行操作，
# 或单击（按钮） 或输入（输入框） ， 下面就来认识 WebDriver 中最常用的几个方法：

# clear()： 清除文本。
# send_keys (value)： 模拟按键输入。
# click()： 单击元素。

from selenium import webdriver
driver=webdriver.Chrome(executable_path='C:\driver\chromedriver74.exe')
driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').clear()
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
driver.quit()

# 提交: submit()
# submit()方法用于提交表单。
# 例如， 在搜索框输入关键字之后的“回车” 操作，
# 就可以通过该方法模拟。
from selenium import webdriver
driver=webdriver.Chrome(executable_path='C:\driver\chromedriver74.exe')
driver.get("https://www.baidu.com")
search_text=driver.find_element_by_id("kw")
search_text.send_keys('selenium')
search_text.submit()
driver.quit()

# 其他常用方法
# size： 返回元素的尺寸。
# text： 获取元素的文本。
# get_attribute(name)： 获得属性值。
# is_displayed()： 设置该元素是否用户可见。
from selenium import webdriver
driver=webdriver.Chrome(executable_path='C:\driver\chromedriver74.exe')
driver.get("http://www.baidu.com")
# 获得输入框的尺寸
size=driver.find_element_by_id("kw").size
print(size)
# 返回百度页面底部备案信息
text=driver.find_element_by_xpath('//*[@id="s-bottom-layer-right"]/span[2]').text
print(text)
# 返回元素的属性值，可以是id,name,type 或其他任意属性
attribute=driver.find_element_by_id("kw").get_attribute("type")
print(attribute)
# 返回元素的结果是否可以见，返回结果为True或False
result=driver.find_element_by_id("kw").is_displayed()
print(result)
driver.quit()
# 执行上面的程序并查看结果：
# size 方法用于获取百度输入框的宽、 高， text 方法用于获得
# 百度底部的备案信息， get_attribute()用于获得百度输入的
# type 属性的值， is_displayed()用于返回一个元素是否可见，
# 如果可见则返回 True， 否则返回 False。











