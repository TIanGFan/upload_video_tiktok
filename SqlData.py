#!/usr/bin/env python
# -*- coding: utf-8 -*
# __author__ = 'LIUTIANFAN'
import sqlite3
import time
import pyperclip as pyperclip

# 建立一个基于硬盘的数据库实例
conn = sqlite3.connect(r"./db/First.db")
# 通过建立数据库游标对象，准备读写操作
db = conn.cursor()


def GetId():
    """查询储存id的值"""

    id_ = db.execute("SELECT * FROM svsa_id where id=1").fetchall()[0][1]
    # print(id_)

    return id_


def GetTitle(title_id):
    """根据查到的id值 查询出标题"""
    get_sql = """SELECT * FROM title_db where id=%s""" % int(title_id)
    title = db.execute(get_sql).fetchall()
    # print('标题：', title[0][0], '\n', '标题id为：', title[0][1])
    print('\033[31m已经复制到剪切板，请用键盘复制标题\033[0m 标题：', title[0][0])
    pyperclip.copy(title[0][0])
    time.sleep(1)
    return title[0]


def Delete(del_title_id):
    """标题上传成功后 删除当前标题 且删除储存 id 的数据"""
    # 删除标题id为   title[0][1]   的记录
    delete_title_sql = """delete from title_db where id=%s""" % int(del_title_id)
    db.execute(delete_title_sql)
    conn.commit()

    """删除储存id为 1 的记录"""
    # delete_svsa_sql = """delete from svsa_id where id=%s""" % int(1)
    db.execute("delete from svsa_id where id=1")
    conn.commit()

    return '标题和储存的 id 删除成功'


def SvsaId(svsa_id):
    """最后存储 id的值 方便后续查询"""
    svsa_sql = """insert into svsa_id Values(1, %s)""" % int(svsa_id+1)
    db.execute(svsa_sql)
    conn.commit()   # 保存提交，确保数据保存成功

    # 关闭与数据库的连接
    # db.close()
    # conn.close()

    return '数据保存成功'

