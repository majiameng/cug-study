from selenium import webdriver
import threading,time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert


window_width = 1920
window_height = 768

def login():
    # 新建页面

     # 用webdriver启动谷歌浏览器
    print("启动浏览器，打开微信公众号登录界面")

    url = "http://sfrz.cug.edu.cn/tpass/login?service=http%3A%2F%2Fstudy.cug.edu.cn%2Fgdlms%2F"
    driver = webdriver.Chrome()
    driver.set_window_size(window_width,window_height) #设置浏览器的窗体大小

    # 打开登录链接
    driver.get(url)



    driver.find_element(By.ID,"qrcode_Login").click()
    print("等待用户打开微信扫描二维码")
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME,'denglu')))
    print("扫描二维码登录成功")

    # driver.find_element(By.ID,"qrcode_Login").click()
    # print("等待用户打开微信扫描二维码")
    # WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME,'denglu')))
    # print("扫描二维码登录成功")

    print (driver.title)

    url = "http://study.cug.edu.cn/gdlms/student/MyStudy/courcelist.do"
    js='window.open("'+url+'");' #通过执行js，开启一个新的窗口

    driver.execute_script(js)
    allhandles=driver.window_handles  #获取当前窗口句柄

    time.sleep(1)
    if driver.current_window_handle==allhandles[1]:
        pass
    else:
        driver.switch_to.window(allhandles[1])#切换窗口


    print (driver.title)

    time.sleep(2)

    trs = driver.find_elements(By.CSS_SELECTOR,".list tr")
    for tr in trs:

        # print()
        tds = tr.find_elements(By.CSS_SELECTOR,"td")
        for td in range(len(tds)):
            if td == 0:
                print("课程名称"+(tds[td].text))
            if td == 1:
                print(tds[td].text)
            if td == 6:
                buttons = tds[td].find_elements(By.CSS_SELECTOR,"input[type='button']")
                for button in range(len(buttons)):
                    if button == 0:
                        buttons[button].click()

                        alert = driver.switch_to.alert.accept()
                        # alert.assertEquals("是否继续学习?", alert.getText())
                        # alert.accept()

                    time.sleep(2)


    time.sleep(2)




    time.sleep(100)

    # driver.get(url)


    # time.sleep(10)

    # driver
    print("点击课程start")
    driver.find_element(By.XPATH,'//*[@id="1"]/td[7]/input[1]').click()
    print("点击课程end")


    time.sleep(1000)
    # page = await browser.newPage()
    #
    # await page.setViewport({'width':window_width,'height':window_height})
    # await page.setUserAgent('Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36')
    #
    # await page.goto(url)


    # cookies = [{'name': 'cas_hash', 'value': '', 'domain': 'sfrz.cug.edu.cn', 'path': '/tpass', 'expires': -1, 'size': 8, 'httpOnly': False, 'secure': False, 'session': True},
    #            {'name': 'Language', 'value': 'zh_CN', 'domain': 'sfrz.cug.edu.cn', 'path': '/', 'expires': 1648564603.981928, 'size': 13, 'httpOnly': False, 'secure': False, 'session': False},
    #            {'name': 'JSESSIONID', 'value': 'l4KyDxPLDu2CDPQzkWh4OXq_zPV3afZoZaI55zG06Xzddm7Nk5W-!-387548016', 'domain': 'sfrz.cug.edu.cn', 'path': '/', 'expires': -1, 'size': 73, 'httpOnly': True, 'secure': False, 'session': True}]
    # await page.setCookie(cookies)


    # 输入Gmail
    # await page.type('#un', username)
    # 点击下一步
    # await page.click('#qrcode_Login')
    # page.mouse  # 模拟真实点击
    #
    # print("等待用户打开微信扫描二维码")
    # await page.waitForNavigation()
    # print("扫描二维码登录成功")
    #
    # # 获取cookies
    # cookie_items = await page.cookies()
    #
    # post = {}
    # # 获取到的cookies是列表形式，将cookies转成json形式并存入本地名为cookie的文本中
    # for cookie_item in cookie_items:
    #     post[cookie_item['name']] = cookie_item['value']
    # cookie_str = json.dumps(post)
    # with open('cookie.txt', 'w+', encoding='utf-8') as f:
    #     f.write(cookie_str)
    # print("cookies信息已保存到本地")

    # 输入password
    # await page.type('#pd input', password)
    # # 点击下一步
    # await page.click('#passwordNext > content > span')
    # page.mouse  # 模拟真实点击
    # time.sleep(10)
    # # 点击安全检测页面的DONE
    # # await page.click('div > content > span')#如果本机之前登录过，并且page.setUserAgent设置为之前登录成功的浏览器user-agent了，
    # # 就不会出现安全检测页面，这里如果有需要的自己根据需求进行更改，但是还是推荐先用常用浏览器登录成功后再用python程序进行登录。
    #
    # # 登录成功截图
    # await page.screenshot({'path': './gmail-login.png', 'quality': 100, 'fullPage': True})
    # #打开谷歌全家桶跳转，以Youtube为例
    # await page.goto('https://www.youtube.com')


if __name__ == '__main__':
    # url = 'https://gmail.com'
    username = '105F24221010'
    password = r'Ma13833886554.'
    login()
    # gmailLogin(username, password)


# 代码由三分醉编写，网址www.sanfenzui.com，参考如下文章：
# https://blog.csdn.net/Chen_chong__/article/details/82950968
