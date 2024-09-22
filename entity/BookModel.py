# -*- coding: utf-8 -*-
"""
图书模块实体类
"""

#图书类
class Book:
    #编号id
    id=None
    #图书名称
    bookName=None
    #图书作者
    author=None
    #图书性别
    sex='男'
    #图书价格
    price=None
    #图书类别id(-1 默认没有选中)
    bookTypeId=-1
    #图书类别描述
    bookDesc=None

    def __init__(self,bookName,author,bookTypeId):
        self.bookName=bookName
        self.author=author
        self.bookTypeId=bookTypeId

    @staticmethod
    def my_constructor(bookName,author,sex,price,bookTypeId,bookDesc):
        obj=Book(bookName,author,bookTypeId)
        obj.sex=sex
        obj.price=price
        obj.bookDesc=bookDesc
        return obj

    @staticmethod
    def my_constructor2(id,bookName,author,sex,price,bookTypeId,bookDesc):
        obj=Book(bookName,author,bookTypeId)
        obj.id=id
        obj.sex=sex
        obj.price=price
        obj.bookDesc=bookDesc
        return obj