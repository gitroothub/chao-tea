from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('D:\chromedriver')
driver.maximize_window()
driver.get("https://chadao-tea.com/contact/")


spec_chars = "!\"#$%&'()*+,-./:1;<=>?@[\]^_`{|}~"
email = 'elonmask@gmail.com'
emailbox = driver.find_element_by_id("contactform-email")
emailbox_notification = driver.find_element_by_class_name("help-block-error")
log = []
for i in spec_chars:
    emailbox.send_keys("elon" + i + "mask@gmail.com")
    emailbox.send_keys(Keys.TAB)
    time.sleep(2)
    if emailbox_notification.text != "Значение «E-mail» не является правильным email адресом.":
        log.append(i)
        emailbox.clear()
    else:
        emailbox.clear()
        

if len(log) == 0:
    print("success")
else:
    print("the following symbols are allowed:\n,", *log)
driver.close()
