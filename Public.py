import sys
sys.path.append(r'/home/peng/learnredis')
from RedisHelper import RedisHelper

obj = RedisHelper()
a='hello world'
obj.public(a)
