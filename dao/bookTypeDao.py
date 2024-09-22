#图书类别数据访问对象
# -*- coding: utf-8 -*-
from entity.BookTypeModel import BookType
from util import dbUtil


def add(bookType:BookType):
    """
    图书类别添加
    :param bookType:图书类别实体
    :return: 返回图形的条数
    """
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        cursor.execute(f"insert into t_booktype values(null,'{bookType.bookTypeName}','{bookType.bookTypeDesc}')")
        #print(cursor.fetchone())  游标打印一次后下次就是空的
        return cursor.rowcount
    except Exception as e:
        con.rollback()
        print(e)
        return 0
    finally:
        dbUtil.closeCon(con)

#搜索/查询
def list(s_bookTypeName:str):
    """
    根据条件查询图书类别信息
    :param s_bookTypeName:图书类别名称
    :return: 返回图书的类别信息集合
    """
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        sql="select * from t_booktype where 1=1"
        if s_bookTypeName.strip() != '':
            sql += "add bookType like '%" + s_bookTypeName +"%' "
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print(e)
        con.rollback()
        return None #无搜索条件返回空
    finally:
        dbUtil.closeCon(con)

#修改
def update(bookType:BookType):
    """
    图书类别修改
    :param s_bookTypeName:图书类别名称
    :return: 返回执行条数
    """
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        cursor.execute(f"update t_booktype set bookTypeName='{bookType.bookTypeName}',bookType='{bookType.bookTypeDesc}' where id={bookType.id}")
        return cursor.rowcount
    except Exception as e:
        con.rollback()
        print(e)
        return 0
    finally:
        dbUtil.closeCon(con)

#删除
def delete(id):
    """
    图书类别修改
    :param id:编号
    :return: 返回执行条数
    """
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        cursor.execute(f"delete from t_booktype where id={id}")
        return cursor.rowcount
    except Exception as e:
        con.rollback()
        print(e)
        return 0
    finally:
        dbUtil.closeCon(con)