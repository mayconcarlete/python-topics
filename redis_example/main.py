import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from redis import Redis
from redis_example.sub import get_value
import time

start_time = time.time()

redis_client = Redis(host='127.0.0.1', port=6379, db=0, password=None, socket_timeout=None)

redis_client.mset({"name":"Carolina"})
# redis_client.mset({'age':1})

# name = redis_client.get('name').decode('utf-8')
# age = redis_client.mget(['age'])[0].decode('utf-8')
# print(name)

# print(age)

# print(type(name))
# print(type(age))

value = get_value('name')

print(value)
print(time.time() - start_time)