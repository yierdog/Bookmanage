from entity.BookTypeModel import BookType
#用户实体类
class User:
    id=None
    username=None
    password=None
    newPassword=None #新密码
    def __init__(self,username,password):
        self.username=username
        self.password=password

    #重载构造法  修改时有3个参数
    @staticmethod
    def my_constructor(username,password,newPassword):
        obj=User(username,password)
        obj.newPassword=newPassword
        return obj
