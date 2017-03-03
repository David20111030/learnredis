import redis

pool = redis.ConnectionPool(host='127.0.0.1',port=6379)

r = redis.Redis(connection_pool=pool)

#pip = r.pipeline(transaction=False)
pipe = r.pipeline(transaction=True)

r.set('name','alex1')
r.set('role','sb1')

#pipe.execute()
