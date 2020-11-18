import pymysql
#打开数据库连接
conn = pymysql.connect('localhost',user = "root",passwd = "aiqiangYUN0716",db = "testdb")
print (conn)
print (type(conn))