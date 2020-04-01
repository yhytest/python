# 控制浏览器操作
# WebDriver提供了set_window_size()方法来设置浏览器的大小
# 以某种浏览器尺寸打开，让访问的页面在这种尺寸下运行。

from selenium import webdriver
driver=webdriver.Chrome(executable_path='C:\driver\chromedriver74.exe')
driver.get("http://www.baidu.com")

# 参数数字为像素点
print("设置浏览器宽480，高800显示")
driver.set_window_size(480,800)
driver.quit()
# 在PC端执行自动化测试脚本大多的情况下是希望浏览器在全屏幕模式下执行，
# 那么可以使用maximize_window()方法使打开的浏览器全屏显示，
# 其用法与set_window_size() 相同，但它不需要参数。

# 控制浏览器后退、前进
# 在使用浏览器浏览网页时，浏览器提供了后退和前进按钮，可以方便地在浏览过的网页之间切换，
# WebDriver也提供了对应的back()和forward()方法来模拟后退和前进按钮。
# 下面通过例子来演示这两个方法的使用。

from selenium import webdriver
driver=webdriver.Chrome(executable_path='C:\driver\chromedriver74.exe')
# 访问百度首页
first_url="http://www.baidu.com"
print("now access %s"%(first_url))
driver.get(first_url)
# 访问新闻页面
second_url="http://news.baidu.com"
print("now access %s "%(second_url))
driver.get(second_url)
# 访问（后退）到百度首页
print("back to %s"%(first_url))
driver.back()
# 前进到新闻页
print(second_url)
driver.forward()
driver.quit()