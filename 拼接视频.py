#!/usr/bin/env python
# -*- coding: utf-8 -*
# __author__ = 'LIUTIANFAN'

# 主要是需要moviepy这个库
from moviepy.editor import *
import os

# 访问 video 文件夹 (假设视频都放在这里面)
for root, dirs, files in os.walk("./video"):
    # 按文件名排序
    files.sort()
    # 遍历所有文件
    for file in files:
        # 如果后缀名为 .mp4
        suffix = os.path.splitext(file)
        if suffix[1] == '.mp4':
            # 拼接成完整路径
            filePath = os.path.join(root, file)

            # 载入准备加入素材的原视频视频
            video = VideoFileClip(filePath)

            # # 载入素材的原视频视频
            # video_source = VideoFileClip('./db/1.mp4')

            # 拼接视频
            final_clip = concatenate_videoclips([video])
            # 生成目标视频文件
            # final_clip.write_videofile(filePath, fps=30, remove_temp=False)
            final_clip.to_videofile("./video/2.mp4", fps=30, remove_temp=False)
