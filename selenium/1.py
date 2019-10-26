from selenium import webdriver
import time

#微博登录

browser = webdriver.Chrome()

def login(username,pwd):
    browser.get("https://passport.weibo.cn/signin/login")
    browser.implicitly_wait(5)
    time.sleep(1)
    #填写登录账号密码
    browser.find_element_by_id("loginName").send_keys(username)
    browser.find_element_by_id("loginPassword").send_keys(pwd)
    time.sleep(1)
    #点击登录
    browser.find_element_by_id("loginAction").click()
    time.sleep()

username = '18530893662'
pwd = 'lvyasen123.'
login(username,pwd)