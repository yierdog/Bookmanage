#图书类别实体类
from pkg_resources import non_empty_lines

#图书类别类
class BookType:
    #编号 主键id
    id = None
    #图书类别名称
    bookTypeName = None
    #图书类别描述
    bookTypeDesc = None

    def __init__(self,bookTypeName,bookTypeDesc):
        self.bookTypeName = bookTypeName
        self.bookTypeDesc = bookTypeDesc

    #重载构造法  修改时有3个参数
    @staticmethod
    def my_constructor(id,bookTypeName,bookTypeDesc):
        obj=BookType(bookTypeName, bookTypeDesc)
        obj.id=id  #动态添加id
        return obj