# -*- coding: utf-8 -*-
# -*- author: GXR -*-

"""
    各种数据库的Python连接方法
    pip install pymysql
    pip install pymongo
    pip install redis
"""

# MySQL
import pymysql

mydb = pymysql.connect(
    host="127.0.0.1",
    user="root",
    passwd="1111",
    db="",
    charset="utf8",
    # 自动保存
    # autocommit=True
)
cur = mydb.cursor()
cur.execute("SELECT VERSION()")
data = cur.fetchall()
print("Database version:", data)
cur.close()
mydb.close()

# MongoDB
import pymongo

myclient = pymongo.MongoClient(host="127.0.0.1", port=27017)
myclient.close()

# Redis
import redis

"""
Redis TCP连接
    redis://[:password]@host:port/db
Redis TCP+SSL连接
    rediss://[:password]@host:port/db
Redis UNIX socket连接
    unix://[:password]@/path/to/socket.sock?db=db
"""

url = "redis://:1111@39.106.189.108:6379/0"
pool = redis.ConnectionPool.from_url(url)
db1 = redis.StrictRedis(connection_pool=pool)
db1.set("name", "Bob")
print(db1.get("name"))

db2 = redis.StrictRedis(host="127.0.0.1", port=6379, password="1111", db=0)
db2.set("name", "Bob")
print(db2.get("name"))
print(db2.dbsize())
print(db2.getset("name", "Mike"))
db2.close()

db3 = redis.Redis(host="127.0.0.1", port=6379, password="1111", db=0)
db3.close()
