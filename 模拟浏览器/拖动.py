from selenium import webdriver
from lxml import etree
from time import sleep
# 导入动作链对应的类
from selenium.webdriver import ActionChains

bro = webdriver.Chrome(executable_path='./chromedriver')

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

# 如果定位的标签是存在于iframe标签中的则必须要通过如下操作再进行标签定位
# 指定浏览器标签作用域
bro.switch_to.frame('iframeResult')
div = bro.find_element_by_id('draggable')

# 动作链
action = ActionChains(bro)
# 点击长按指定的标签
action.click_and_hold(div)

for i in range(5):
    # 移动偏移像素，执行
    action.move_by_offset(17, 0).perform()
    sleep(0.3)

# 释放动作链
action.release()

bro.quit()

print(div)
