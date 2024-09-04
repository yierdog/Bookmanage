# -*- coding: utf-8 -*-
"""
用户模块-数据访问对象
"""
from entity.UserModel import User
from util import dbUtil


def login(user:User):
    """
    用户登录判断
    :param user: 用户实体
    :return: 登录成功返回用户信息实体，登录失败，返回None
    """
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        cursor.execute(f"select * from t_user where username ='{user.username}' and password='{user.password}'")
        #print(cursor.fetchone())  游标打印一次后下次就是空的
        return cursor.fetchone()
    except Exception as e:
        con.rollback()
        print(e)
        return None
    finally:
        dbUtil.closeCon(con)