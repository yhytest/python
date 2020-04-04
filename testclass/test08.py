# 获取断言信息
# 我们通常可以通过获取title 、URL和text等信息进行断言。
# text方法在前面已经讲过，它用于获取标签对之间的文本信息。
# 下面同样以百度为例，介绍如何获取这些信息。
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome(executable_path='C:\driver\chromedriver74.exe')
driver.get("https://www.baidu.com")
print('Before seach======')
# 打印当前页面title
title=driver.title
print(title)
# 打印当前页面URL
now_url=driver.current_url
print(now_url)
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(1)

print('After search=======')
# 再次打印当前页面title
title=driver.title
print(title)

# 打印当前页面url
now_url=driver.current_url
print(now_url)

# 获取结果数目,优先使用复数，因为class_name具有广泛性，用的比例高，出现复数的概率大。优先被使用
# 只有判断容器的长度为1的时候，才会用find_element_by_class_name
user=driver.find_element_by_class_name('nums_text')
# 先判断对象的类型，根据类型找方法
print(type(user))
# print(len(user))
print(user.text)
driver.quit()

# title：用于获得当前页面的标题。
# current_url：用户获得当前页面的URL。
# text：获取搜索条目的文本信息。
