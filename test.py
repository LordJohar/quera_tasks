import redis
# r = redis.StrictRedis()
#r = redis.Connection(host="192.168.32.86", port=6379, db=0)

# r.set("counter", 40)
# r.set("first", 1)
# print(r.get("counter").decode("utf-8"))
# if "first" in r.keys():
#     print("if")
# elif "first" in r.keys().decode("utf-8"):
#     print("elif")
# else:
#     print("where?????")

# r.keys("first")



pool = redis.ConnectionPool(host="192.168.32.86", port=6379, db=0)
redis_conn = redis.Redis(connection_pool=pool)

print(redis_conn.keys())