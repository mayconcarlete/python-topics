from redis import Redis

redis_client = Redis(host='127.0.0.1', port=6379, db=0, password=None, socket_timeout=None)

def get_value(key):
    return redis_client.mget([key])