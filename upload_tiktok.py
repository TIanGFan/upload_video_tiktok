#!/usr/bin/env python
# -*- coding: utf-8 -*
# __author__ = 'LIUTIANFAN'
import os
import time
from selenium import webdriver
from collections import deque
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from SqlData import GetId, GetTitle, Delete, SvsaId
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, ElementClickInterceptedException

chromedriver = r'./venv/Scripts/chromedriver.exe'  # 浏览器驱动文件的路劲
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("proxy-server=socks5://127.0.0.1:1081")  # 加 socks5 代理
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:1088")  # 打开固定 页面
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)  # 初始化浏览器
# browser.get("https://whoer.net/")


# 存放视频文件路劲的
video_file_path = deque()
# 存放视频文件个数的
video_len = []
# 上传文件开始 的数
file_upload = 1


def VideoPath(path):
    """获取文件夹下共有多少个视频文件 并生成从到小的视频文件名排列"""
    file_path = os.listdir(path)
    print('一共有 {} 条视频，准备修改文件的 MD5 值'.format(len(file_path)))
    # # 存入视频文件个数的
    video_len.append(len(file_path))
    for i in range(len(file_path)+1):
        video_name = os.path.join(path, 'my_' + str(i) + '.mp4')
        # 存入视频文件的路劲
        video_file_path.append(video_name)
    """    1with open(video_name, "a") as f:
            f.write("####&&&&")
    print("{} 个文件的 MD5 值修改成功".format(len(file_path)))"""
    return UploadVideo(path)


def UploadVideo(path_name):
    """上传视频文件"""
    global file_upload
    # 退出当前iframe页面
    browser.switch_to.parent_frame()
    time.sleep(3)
    title = GetTitle(GetId())
    # 存放视频文件名的 最后删除视频所用
    delete_list = []
    # 判断是否是 上传视频 页面 不是就进入
    if browser.title != '上傳 | TikTok':
        url = r'https://www.tiktok.com/upload?lang=zh-Hant-TW'
        print('进入上传页面,请等待两分钟，让网页全部加载完成！')
        browser.get(url)
        time.sleep(120)
    print(browser.get_cookies())
    iframe = browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/iframe')  # 定位到iframe
    # 设置等待时间
    wait = WebDriverWait(browser, 240)
    wait.until(ec.frame_to_be_available_and_switch_to_it(iframe))  # 进入iframe 显示等待 60
    print('进入iframe页面')

    # 上传视频
    browser.find_element(By.TAG_NAME, 'input').send_keys(video_file_path.pop())
    print('正在上传第 {} / {} 个视频中，请等待...'.format(file_upload, video_len[0]))

    try:
        # 定位到正在取消
        upload_ = '//*[@id="root"]/div/div/div/div/div[2]/div[1]/div/div/button/div/div'
        upload = wait.until(ec.visibility_of_element_located((By.XPATH, upload_)))
        # 当 upload 等于 取消的时候 一直获取 上传进度
        while upload.text == '取消':
            upload_100 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div")  # 上传进度
            print('\r', "上传进度为 {} {}".format(upload_100.text, upload.text), end='')
            time.sleep(1)
    except StaleElementReferenceException:
        pass

    try:
        # 上传成功
        # 获取到正在上传的 文件名称
        print('\n', '获取到正在上传的 文件名称')
        uploading = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div[1]/div').text
        # 存放视频名称 上传完成后删除视频
        delete_list.append(uploading)
        canvas = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div[2]')
        if canvas.text == '變更影片':
            print('第一个视频 {} 上传成功\n'.format(uploading))
    except StaleElementReferenceException:
        pass

    # 输入标题
    try:
        try:
            # 先判断封面图是否显示出来 显示出来了后再输入标题
            print("等待页面封面图显示当中\n")
            fm = '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[3]/div/div[1]/img[2]'
            wait.until(ec.visibility_of_element_located((By.XPATH, fm)))  # 进入iframe 显示等待 60
            print("封面图已经存在")

        except StaleElementReferenceException:
            pass

        try:
            bj = '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[1]/div[2]/button'
            # 进入 编辑 页面
            element = browser.find_element(By.XPATH, bj)
            # 使用js 点击方式 点击 编辑按钮
            browser.execute_script("arguments[0].click();", element)
            bj_1 = '//*[@id="tux-portal-container"]/div[2]/div/div/div/div/div[2]/div/div[3]/div[3]/div/div[1]/div/div/div/div[4]/div[1]'
            # 点击 编辑标题
            wait.until(ec.visibility_of_element_located((By.XPATH, bj_1))).click()

            yu_1 = '//*[@id="tux-portal-container"]/div[2]/div/div/div/div/div[2]/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div/div[' \
                   '1]/div/div/div/div/div/div/span[1]/span '
            # 判断 编辑 页面 标题栏是否有内容 先清空输入栏
            yu_ = wait.until(ec.visibility_of_element_located((By.XPATH, yu_1)))
            if yu_.text:
                print(yu_.text)
                print('清空标题栏')
                yu_.clear()

            # 关闭编辑 页面
            gb = '//*[@id="tux-portal-container"]/div[2]/div/div/div/div/div[2]/div/div[1]/span/div/div[2]'
            browser.find_element(By.XPATH, gb).click()
            # 确认关闭 编辑 页面
            gb_1 = '//*[@id="tux-portal-container"]/div[5]/div/div/div/div/div[2]/div/div/button[1]/div/div'
            browser.find_element(By.XPATH, gb_1).click()
            time.sleep(3)
            # 判断标题栏是否有内容 先清空输入栏
            yu = '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/span[1]/span'
            yu_2 = wait.until(ec.visibility_of_element_located((By.XPATH, yu)))
            if yu_2.text:
                print(yu_2.text)
                print('清空标题栏')
                yu_2.clear()

            # 输入标题
            time.sleep(0.5)
            title_xpath = '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div'
            title_ = browser.find_element(By.XPATH, title_xpath)
            title_.send_keys(Keys.CONTROL, 'a')
            title_.send_keys(Keys.CONTROL, 'v')
            print('标题输入完毕')
            time.sleep(2)
        except (StaleElementReferenceException, NoSuchElementException):
            pass
    except StaleElementReferenceException:
        pass

    # 执行版本检查
    try:
        gits = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[6]/div[2]/div')
        gits.click()
        time.sleep(1)
        version = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[7]/div/span')
        print('开始版本检查：', version.text)
        while version:
            if version.text == '正在檢查。這將需要約 1 分鐘的時間。':
                time.sleep(1)
                continue
            elif version.text == '未偵測到任何問題。':
                print('版本检查完毕：', version.text)
                break
            else:
                print('出现错误：', version.text)
    except StaleElementReferenceException:
        pass

    # 发布视频
    try:
        try:
            # 点击发布按钮
            release = browser.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[8]/div[2]/button')
            release.click()
            rase_vd_up_ = '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[9]/div/div[1]/div/div[2]/span'
            rase_vd_up = wait.until(ec.visibility_of_element_located((By.XPATH, rase_vd_up_)))
            if rase_vd_up:
                print('视频上传等待中...')
        except StaleElementReferenceException:
            pass
        except NoSuchElementException:
            pass
        
        try:
            # 正在上传当中
            rase_vd_up_ = '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[9]/div/div[1]/div/div[2]/span'
            rase_vd_up = wait.until(ec.visibility_of_element_located((By.XPATH, rase_vd_up_)))
            while rase_vd_up.text == '正在上傳':
                print('\r', "正在上传当中...", end='')
                time.sleep(1)
        except StaleElementReferenceException:
            pass
        except NoSuchElementException:
            pass
        print("上传完毕！1", '\n')
        release_up = '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[9]/div/div[1]'
        release_up_ = wait.until(ec.visibility_of_element_located((By.XPATH, release_up)))
        while release_up_.text != '正在將你的影片上傳至 TikTok！':
            print('\r', "正在发布当中...", end='')
            time.sleep(1)
    except StaleElementReferenceException:
        pass

    print('\n', '{} 视频发布成功！'.format(delete_list[0]))
    # 发布完视频将该视频标签以及该视频进行删除
    # 删除视频
    os.remove(os.path.join(path_name, delete_list[0]))  # 删除文件
    # 删除标题
    Delete(GetId())
    # 保存完下一个标题id
    SvsaId(title[1])
    print('删除视频以及该视频标题和保存下一个标题id成功')

    # 继续上传其他视频
    continue_to_upload_ = '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[9]/div/div[2]/div[1]'
    continue_to_upload = wait.until(ec.visibility_of_element_located((By.XPATH, continue_to_upload_)))
    if continue_to_upload.text == '上傳其他影片':
        continue_to_upload.click()
        # 视频计数加1
        file_upload += 1
        # 重复执行本函数
        UploadVideo(path_name)
        # 退出当前iframe页面
        browser.switch_to.parent_frame()
        print('继续上传其他视频')
    return '1'


if __name__ == "__main__":
    # 输入视频文件所在文件夹绝对路径
    # video_path = input()
    video_path = r'C:\Users\Administrator\Desktop\DOUYIN_video\video\善喜说女装--110567985801'
    VideoPath(video_path)


