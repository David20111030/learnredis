#!/usr/bin/env python3
__author__ = 'Eva_J'

import redis
#r = redis.Redis(host='127.0.0.1', port=6379)
r = redis.Redis(host='127.0.0.1', port=6379 ,password=1234)
r.set('city','sz')
print (r.get('city'))
print (r.get('name'))
