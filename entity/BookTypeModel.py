#ͼ�����ʵ����
from pkg_resources import non_empty_lines

#ͼ�������
class BookType:
    #��� ����id
    id = None
    #ͼ���������
    bookTypeName = None
    #ͼ���������
    bookTypeDesc = None

    def __init__(self,bookTypeName,bookTypeDesc):
        self.bookTypeName = bookTypeName
        self.bookTypeDesc = bookTypeDesc

    #���ع��취  �޸�ʱ��3������
    @staticmethod
    def my_constructor(id,bookTypeName,bookTypeDesc):
        obj=BookType(bookTypeName, bookTypeDesc)
        obj.id=id  #��̬���id
        return obj