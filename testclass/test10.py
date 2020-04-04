# 定位一组元素
# webDriver还提供了8种用于定位一组元素的方法
# find_elements_by_id()
# find_elements_by_name()
# find_elements_by_class_name()
# find_elements_by_tag_name()
# find_elements_by_link_text()
# find_elements_by_partial_link_text()
# find_elements_by_xpath()
# find_elements_by_css_selector()
# 定位一组元素的方法与定位单个元素的方法类似，
# 唯一的区别是在单词element后面多了一个s表示复数。
# 接下来通过例子演示定位一组元素的使用：
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome(executable_path='C:\driver\chromedriver74.exe')
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(1)
# 定位一组元素
texts=driver.find_elements_by_xpath('//div/h3/a')
print(type(texts))
print(len(texts))
# x循环遍历出每一条搜索结果的标题
for t in texts:
    print(t.text)
    print(type(t))
    driver.quit()

