#!/usr/bin/env python
# -*- coding: utf-8 -*
# __author__ = 'LIUTIANFAN'
import os
import sqlite3

# 存放视频文件个数的
video_len = []


def VideoPath(path):
    """获取文件夹下共有多少个视频文件 并生成从到小的视频文件名排列"""
    file_path = os.listdir(path)
    for i in range(len(file_path)):
        video_name = os.path.join(path, 'my_', str(i), 'mp4')
        video_len.insert(0, video_name)
    return video_len


if __name__ == "__main__":
    # 输入视频文件所在文件夹绝对路径
    # video_path = input()
    video_path = r'C:\Users\Administrator\Desktop\DOUYIN_video\video\善喜说女装--110567985801'
    VideoPath(video_path)
