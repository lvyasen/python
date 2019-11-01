from selenium import webdriver
import time, json

# 微博登录

browser = webdriver.Chrome()


# 加好友
def add_friends(uid):
    browser.get("https://m.weibo.com/u/" + str(uid))
    browser.implicitly_wait(5)
    follow_btn = browser.find_element_by_xpath('//div[@class="m-add-box m-followBtn"]')
    follow_btn.click()
    time.sleep(1)
    # 选择分组
    group_btn = browser.find_element_by_xpath(
        "/html/body/div[@id='app']/div[1]/div[2]/div[@class='m-pop m-pop-lt']/section/ul[@class='gp-list']/li[7]/label[@class='m-checkbox']")
    group_btn.click()
    time.sleep(1)
    sure_btn = browser.find_element_by_xpath(
        "/html/body/div[@id='app']/div[1]/div[2]/div[@class='m-pop m-pop-lt']/footer[@class='m-btm-btns m-box']/div[@class='m-box-col'][2]/a[@class='m-btn m-btn-white m-btn-text-orange']")
    sure_btn.click()


# 发微博
def post_content(content):
    browser.get('https://m.weibo.cn/compose/')
    browser.implicitly_wait(2)

    content_textarea = browser.find_element_by_xpath("//span[@class='m-wz-def']/textarea").send_keys(content)
    time.sleep(1)
    post_submit = browser.find_element_by_xpath("//a[@class='m-send-btn']").click()


def login(username, pwd):
    browser.get("https://passport.weibo.cn/signin/login")
    browser.implicitly_wait(2)
    time.sleep(1)
    # 填写登录账号密码
    browser.find_element_by_id("loginName").send_keys(username)
    browser.find_element_by_id("loginPassword").send_keys(pwd)
    time.sleep(1)
    # 点击登录
    browser.find_element_by_id("loginAction").click()
    time.sleep(1)
    # 获取cookie
    # cookie_list = browser.get_cookies()
    # print(cookie_list)
    # login_json = open('login_cookie.json', 'w')
    # login_json.write(json.dumps(cookie_list))


    # content = "你们看“肖战小号”这个事了吗？有黑粉用时1个月，养了3个微博账号，通过伪造行程定位、盗图、伪造情侣头像等手段，冒充是肖战的小号，冒充肖战的工作人员的账号，故意误导吃瓜群众认为他有男友。结果被另一波黑粉撞破，提前暴露了。"
    # post_content(content)
    # add_friends(1618051664)


username = '18530893662'
pwd = 'lvyasen123.'


login(username, pwd)
def login_cookie():
    cookie_list = open("login_cookie.json")
    cookie_data = cookie_list.read()
    # cookie_data = json.loads(cookie_data)
    # print(cookie_data)
    # for c in cookie_data:
    #     browser.add_cookie(cookie_dict=c)

    # time.sleep(3)
    # browser.get("https://m.weibo.cn/")



