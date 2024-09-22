# -*- coding: utf-8 -*-
"""
用户模块-数据访问对象
"""
from entity.UserModel import User
from utill import dbUtil


#记录当前登录用户
currentUser:User=None

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

#修改
def modifyPassword(user:User):
    """
    修改密码
    :param s_bookTypeName:用户实体
    :return: 返回执行条数
    """
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        cursor.execute(f"update t_user set password='{user.newPassword}' where username='{user.username}'")
        return cursor.rowcount
    except Exception as e:
        con.rollback()
        print(e)
        return 0
    finally:
        dbUtil.closeCon(con)