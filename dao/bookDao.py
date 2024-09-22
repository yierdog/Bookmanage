#图书数据访问对象（外键）
# -*- coding: utf-8 -*-
from entity.BookModel import Book
from utill import dbUtil
def countBypeId(typeId):
    """
    根据图书类别id查询图书数量
    :param typeId:
    :return:
    """
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        cursor.execute(f"select count(*) as total from t_book where bookTypeId={typeId}")
        return cursor.fetchone()
    except Exception as e:
        con.rollback()
        print(e)
        return None
    finally:
        dbUtil.closeCon(con)

def add(book:Book):
    """
    图书添加
    :param bookType:图书类别实体
    :return: 返回图形的条数
    """
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        cursor.execute(f"insert into t_book values(null,'{book.bookName}','{book.author}','{book.sex}',{book.price},{book.bookTypeId},'{book.bookDesc}')")
        return cursor.rowcount
    except Exception as e:
        con.rollback()
        print(e)
        return 0
    finally:
        dbUtil.closeCon(con)

 #根据条件搜索图书信息
def list(s_book:Book):
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        sql="select t.id as id,t.bookName,author,bookTypeName,sex,price,bookDesc from t_book as t,t_booktype as ty where t.bookTypeId=ty.id"
        if s_book!=None:
            if s_book.bookName.strip() != '':
                sql += " and t.bookName like '%" + s_book.bookName +"%' "
            if s_book.author.strip() != '':
                sql += " and t.author like '%" + s_book.author + "%' "
            if s_book.bookTypeId != -1:
                sql += " and t.bookTypeId = " + str(s_book.bookTypeId)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print(e)
        con.rollback()
        return None #无搜索条件返回空
    finally:
        dbUtil.closeCon(con)
#修改
def update(book:Book):
    """
    图书修改
    :param book:图书名称
    :return: 返回执行条数
    """
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        cursor.execute(f"update t_book set bookName='{book.bookName}',author='{book.author}',sex='{book.sex}',price='{book.price}',bookTypeId='{book.bookTypeId}',bookDesc='{book.bookDesc}' where id={book.id}")
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
    图书修改
    :param id:编号
    :return: 返回执行条数
    """
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        cursor.execute(f"delete from t_book where id={id}")
        return cursor.rowcount
    except Exception as e:
        con.rollback()
        print(e)
        return 0
    finally:
        dbUtil.closeCon(con)