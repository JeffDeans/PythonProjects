import pymysql

conn = pymysql.connect(host="10.51.1.16", user="root", password="Rh123456", database="lis")
##创建一个光标对象
cursor = conn.cursor()
# 定义要执行的SQl
sql = '''
SELECT substring_index(HOST, ':', 1) AS host_name,state,count(*) AS count FROM information_schema.PROCESSLIST GROUP BY state,host_name order by count desc;
'''
# 使用 execute()  方法执行 SQL 查询
cursor.execute(sql)
# 使用 fetchone() 方法获取数据
data = cursor.fetchall()
print(data)
