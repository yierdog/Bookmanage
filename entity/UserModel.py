from entity.BookTypeModel import BookType
#�û�ʵ����
class User:
    id=None
    username=None
    password=None
    newPassword=None #������
    def __init__(self,username,password):
        self.username=username
        self.password=password

    #���ع��취  �޸�ʱ��3������
    @staticmethod
    def my_constructor(username,password,newPassword):
        obj=User(username,password)
        obj.newPassword=newPassword
        return obj
