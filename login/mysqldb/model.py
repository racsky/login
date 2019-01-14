import pymysql

db = pymysql.connect('localhost','root','123456')

# 创建游标
cursor = db.cursor()

# 创建数据库
sql = "create database chatroom character set utf8"
sql1 = "use chatroom"

# 创建数据表
sql2 = "create table user (id int primary key auto_increment,\
     name varchar(32),\
     account varchar(24),\
     password varchar(24),\
     integral int,\
     emailid varchar(24),\
     createtime timestamp)"

# 执行
cursor.execute(sql)
cursor.execute(sql1)
cursor.execute(sql2)

# 提交
db.commit()
db.close()

print('create ok')
