# coding=gb2312
# 数据库连接工具包
from pymysql import Connection


# 获取数据库连接
def getCon():
    con = Connection(
        host='localhost',
        port=3306,
        user='root',
        password='TJP0596',
        database='book',
        autocommit=True  # 设置自动提交
    )
    return con


# 关闭数据库连接
def closeCon(con: Connection):
    if con:
        con.close()


# 测试
if __name__ == '__main__':
    con = None
    try:
        con = getCon()
        cursor = con.cursor()
        cursor.execute("select * from  t_user")
        print(cursor.fetchall())
    except Exception as e:
        print(e)
    finally:
        closeCon(con)
