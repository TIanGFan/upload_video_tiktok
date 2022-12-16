#!/usr/bin/env python
# -*- coding: utf-8 -*
# __author__ = 'LIUTIANFAN'
import os


def MeName(path_):
    print(path_)
    file_list = os.listdir(path_)
    print(file_list, '\n')
    for fi in file_list:
        print(fi)
        old_dir = os.path.join(path_, fi)
        print(old_dir)
        # filename = "my" + str(i + 1) + "." + str(fi.split(".")[-1])
        # print(filename, '\n')
        head, sep, tail = fi.partition('_')
        filename = "my" + '_' + head + "." + str(fi.split(".")[-1])
        print(filename)

        """new_dir = os.path.join(path_, filename)
        print(new_dir, '\n')
        try:
            os.rename(old_dir, new_dir)
        except Exception as e:
            print(e)
            print("Failed!")
        else:
            print("SUcess!")"""


if __name__ == "__main__":
    path_1 = r'C:\Users\Administrator\Desktop\DOUYIN_video\video\善喜说女装--110567985801'
    MeName(path_1)
