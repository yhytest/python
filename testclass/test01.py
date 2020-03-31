# 安装selenium
# 依赖不能正确安装的时候，请在cmd里输入以下的方法
# python -m pip install --upgrade pip 更新pip版本，默认版本不支持Https协议
# 方法1：增大超时时间
# pip --default-timeout=100 install selenium
# 方法2：修改安装源为清华安装源
# pip install --index https://mirrors.ustc.edu.cn/pypi/web/simple/ selenium

#从selenium模块中导入webdriver的驱动
from selenium import webdriver
#调用驱动路径并赋值给driver这个对象
driver=webdriver.Chrome(executable_path="C:\driver\chromedriver74.exe")
#driver调用get的方法访问www.baidu.com
driver.get("http:www.baidu.com")
#打印driver的内容的标题
print(driver.title)
#driver停止运行
driver.quit()
