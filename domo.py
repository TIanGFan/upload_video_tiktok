#!/usr/bin/env python
# -*- coding: utf-8 -*
# __author__ = 'LIUTIANFAN'
import time
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# 指定驱动的路劲
path = r'./venv/Scripts/chromedriver.exe'
# 无界面的浏览器
# option = webdriver.ChromeOptions()
# option.add_argument("headless") 主要隐藏代码
# browser = webdriver.Chrome(executable_path=path, options=option)
# 初始化 有画面的 浏览器
# browser = webdriver.Chrome(path)
# browser.get(r'https://www.tiktok.com/upload?lang=zh-Hant-TW')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('lang=zh-CN,zh,zh-TW,en-US,en')
chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
# 加socks5代理
chrome_options.add_argument("proxy-server=socks5://127.0.0.1:1081")
browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
# browser.get("https://whoer.net/")
browser.get(r'https://www.tiktok.com/upload?lang=zh-Hant-TW')
# 不关闭浏览器
ActionChains(browser).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()

# 查看网页标题 后期判断是登录页面还是上传页面
title = browser.title
print(title)
if title == '登入 | TikTok':
    # 设置等待最长时间 100 秒 每次检测的间隔时间为 2 秒
    wait = WebDriverWait(browser, 20, 2)
    # 设置判断条件为 谷歌登录按钮出现 然后点击
    google_login = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[4]")))
    print(google_login)
    google_login[0].click()

    print(1)
    time.sleep(20)
elif title == '上傳  | TikTok':
    pass
else:
    pass
# 关闭浏览器
browser.quit()
# browser.close()
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# 设置等待时间为 100 秒 每次检测间隔时间为 2 秒
wait = WebDriverWait(browser, 100, 2)
print('等待页面加载')
# 设置判断条件 等待 iframe 子页面加载完成
frame = wait.until(ec.presence_of_all_elements_located((By.TAG_NAME, 'iframe')))
# frame = wait.until(ec.visibility_of_element_located((By.TAG_NAME, 'iframe')))
"""



