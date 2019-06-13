import pymysql

# xsmart_users

# -------------------------------------------------------------------------------
# 函数/过程名称：ReadMySQLData
# 函数/过程的目的：写MySQL数据库单条数据
# 假设：无
# 影响：无
# 输入：无
# 返回值：查询一行数据（元组类型）
# 创建者：老道
# 创建时间：2019/05/26
# 修改者：
# 修改原因：
# 修改时间:
# -------------------------------------------------------------------------------

def ReadMySQLData(sql,host='192.168.1.100',port=3306,user='edu',password='edu',db='edu'):
    try:
        conn = pymysql.connect(host=host,port=port,user=user,password=password,db=db)
        curs = conn.cursor()
        curs.execute(sql)
        r = curs.fetchone()
        curs.close()
        conn.close()
        return r
    except BaseException as msg:
        print(msg)

# print( ReadMySQLData('select * from xsmart_users where username="18618492915"'))