#键盘事件
# Keys()类提供了键盘上几乎所有按键的方法。
# 前面了解到， send_keys()方法可以用来模拟键盘输入，
# 除此 之外， 我们还可以用它来输入键盘上的按键，
# 甚至是组合键， 如 Ctrl+A、 Ctrl+C 等。

from selenium import webdriver
# 引入keys模块
from selenium.webdriver.common.keys import keys
driver=webdriver.Chrome(executable_path='C:\driver\chromedriver74.exe')
driver.get("http://www.baidu.com")
# 输入框输入内容
driver.find_element_by_id("kw").send_keys("seleniumm")
# 删除多输入的一个m
driver.find_element_by_id("kw").send_keys(keys.BACK_SPACE)
# 输入空格键+“教程”
driver.find_element_by_id("kw").send_keys(keys.SPACE)
driver.find_element_by_id("kw").send_keys("教程")
# ctrl+a全选输入框内容
driver.find_element_by_id("kw").send_keys(keys.CONTROL,'a')
# ctrl+x剪切输入框内容
driver.find_element_by_id("kw").send_keys(keys.CONTROL,'x')
# ctrl+v粘贴内容到输入框
driver.find_element_by_id("su").send_keys(keys.CONTROL,'v')
# 通过回车键来代替单击操作
driver.find_element_by_id('su').send_keys(keys.ENTER)
driver.quit()
# 需要说明的是， 上面的脚本没有什么实际意义， 仅向我们展示模拟键盘各种按键与组合键的用法。
# from selenium.webdriver.common.keys import Keys
# 在使用键盘按键方法前需要先导入 keys 类。
# 以下为常用的键盘操作：
# send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
# send_keys(Keys.SPACE) 空格键(Space)
# send_keys(Keys.TAB) 制表键(Tab)
# send_keys(Keys.ESCAPE) 回退键（Esc）
# send_keys(Keys.ENTER) 回车键（Enter）
# send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
# send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
# send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
# send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）
# send_keys(Keys.F1) 键盘 F1
# send_keys(Keys.F12) 键盘 F12