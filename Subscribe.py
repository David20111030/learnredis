import sys
sys.path.append(r'/home/peng/learnredis')
from RedisHelper import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()

while True:
	msg= redis_sub.parse_response()
	print (msg)
