"""
  用户实体类
"""

#用户实体类
class User:
    id=None
    username=None
    password=None
    def __init__(self,username,password):
        self.username=username
        self.password=password