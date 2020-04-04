# 多表单切换
# 在Web应用中经常会遇到frame/iframe表单嵌套页面的应用，WebDriver只能在一个页面上对元素识别与定位，对于frame/iframe表单内嵌页面上的元素无法直接定位。这时就需要通过switch_to.frame()方法将当前定位的主体切换为frame/iframe表单的内嵌页面中。
# <html>
#   <body>
#     ...
#     <iframe id="x-URS-iframe" ...>
#       <html>
#          <body>
#            ...
#            <input name="email" >
# 126邮箱登录框的结构大概是这样子的，想要操作登录框必须要先切换到iframe表单。
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("http://www.126.com")
# driver.switch_to.frame('x-URS-iframe')
# driver.find_element_by_name("email").clear()
# driver.find_element_by_name("email").send_keys("username")
# driver.find_element_by_name("password").clear()
# driver.find_element_by_name("password").send_keys("password")
# driver.find_element_by_id("dologin").click()
# driver.switch_to.default_content()
# driver.quit()
# switch_to.frame() 默认可以直接取表单的id 或name属性。如果iframe没有可用的id和name属性，
# 则可以通过下面的方式进行定位。


#先通过xpth定位到iframe
xf=driver.find_element_by_xpath('//*[@id="x-URS-iframe"]')
# 再将定位对象传给switch_to.frame()方法
driver.switch_to.frame(xf)
...
driver.switch_to.parent_frame()
# 除此之外，在进入多级表单的情况下，还可以通过switch_to.default_content()跳回最外层的页面。