from typing import Counter
from flask import Flask, request
import redis
# import time
from ratelimit import limits, RateLimitException
from backoff import on_exception, expo

import requests

app = Flask(__name__)

pool = redis.ConnectionPool(host="192.168.32.86", port=6379, db=0)
redis_conn = redis.Redis(connection_pool=pool)

LIMIT_TIME = 60

@limits(calls=15, period=LIMIT_TIME)
@app.route('/')
def redis_count():
    header=request.headers.get('CLIENT-KEY')
    if header is None or header == 'null':
        pass
    elif bytes(header, 'utf-8') in redis_conn.keys() :
        Counter = int(redis_conn.get(header).decode("utf-8"))+1
        redis_conn.set(header, Counter)
    else:
        redis_conn.set(header, 1)
    data = {}
    keys = redis_conn.keys()
    for key in keys:
        c = redis_conn.get(key)
        data[key.decode('utf-8')] = int(c.decode('utf-8'))

    response = {'state': data}
    return response


# dict_response={}
# @app.route('/')
# def cnt():
#     client_key=request.headers.get('CLIENT-KEY')
#     if client_key is None or client_key == 'null':
#         pass
#     elif client_key in dict_response.keys():
#         dict_response[client_key] += 1
#     else:
#         dict_response[client_key] = 1
#     response = {'state': dict_response}
#     return response



# keys=[]
# counters=[]
# @app.route('/')
# def counter():
#     # get headers and store in list
#     if request.headers.get('CLIENT-KEY') is None or request.headers.get('CLIENT-KEY') == 'null':
#         pass
#     elif request.headers.get('CLIENT-KEY') in keys:
#         counters[keys.index(request.headers.get('CLIENT-KEY'))] += 1
#     else:
#         keys.append(request.headers.get('CLIENT-KEY'))
#         counters.append(1)
    
#     pre_response = dict(zip(keys,counters))
#     response = {'state': pre_response}
#     return response



if __name__ == "__main__":
    app.run()


{
        "1": 4,
        "2": 7,
        "a": 12,
        "ab": 3,
        "b": 4,
        "one": 4,
        "two": 1
}