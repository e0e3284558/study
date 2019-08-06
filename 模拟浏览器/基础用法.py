from selenium import webdriver
from lxml import etree
from time import sleep

# 实例化浏览器对象（传入浏览器对象驱动）
bro = webdriver.Chrome(executable_path='./chromedriver')

# 编写基于浏览器自动化的操作代码
# 让浏览器发起一个指定url对应的请求
# bro.get('http://125.35.6.84:81/')   // 打不开页面则报错
# bro.get('https://www.baidu.com')
bro.get('http://mpa.gd.gov.cn/ztzl/zdly/xyxx/index.html')
page_text = bro.page_source
# 解析企业名称
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="lists"]/div[1]/ul/li')
for li in li_list:
    name = li.xpath('./h4/a/text()')
    print(name)

sleep(5)
# 关闭浏览器
bro.quit()
