import pymysql
from dbutils.pooled_db import PooledDB
import time
import schedule


class cal_mysql_conn:
    def __init__(self):
        self.host = "10.98.1.4"
        self.user = "root"
        self.password = "ruihua123456"
        self.database = "lis"
        self.conn = PooledDB(
            pymysql,
            host=self.host,
            user=self.user,
            passwd=self.password,
            db=self.database,
            port=3306,
        ).connection()
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        self.sql = """ SELECT substring_index(HOST, ':', 1) AS host_name, user, count(*) AS count FROM information_schema.PROCESSLIST GROUP BY host_name order by count desc;
                             """
        # schedule.every(5).seconds.do(self.cursor.execute(self.sql))
        for n in range(180):
            try:
                time.sleep(5)
                self.cursor.execute(self.sql)
                self.data = self.cursor.fetchall()
                for i in self.data:
                    print(i)
                print("-------------------------------------")
            except ConnectionError as e:
                print(e)
        self.cursor.close()
        self.conn.close()
        print("数据库连接关闭了")


if __name__ == "__main__":
    mysql_conn = cal_mysql_conn()
