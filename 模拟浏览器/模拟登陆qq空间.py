from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='./chromedriver')
bro.get('https://qzone.qq.com')
bro.switch_to.frame('login_frame')
bro.find_element_by_id("switcher_plogin")
a_tag = bro.find_element_by_id('switcher_plogin')
a_tag.click()

userName_tag = bro.find_element_by_id('u')
password_tag = bro.find_element_by_id('p')

sleep(1)
userName_tag.send_keys('1013284558')
sleep(1)
password_tag.send_keys('******..')
sleep(1)
btn = bro.find_element_by_id('login_button')
btn.click()
sleep(4)
bro.quit()
