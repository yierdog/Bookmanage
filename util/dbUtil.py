# coding=gb2312
# ���ݿ����ӹ��߰�
from pymysql import Connection


# ��ȡ���ݿ�����
def getCon():
    con = Connection(
        host='localhost',
        port=3306,
        user='root',
        password='TJP0596',
        database='book',
        autocommit=True  # �����Զ��ύ
    )
    return con


# �ر����ݿ�����
def closeCon(con: Connection):
    if con:
        con.close()


# ����
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
