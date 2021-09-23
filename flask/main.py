import asyncio
from flask import Flask, jsonify
import asyncio
from asyncio.tasks import gather
from typing import List
import time

app = Flask('My Flask')



@app.route('/multiple', methods=['GET'])
async def index():
    start_time = time.time()
    data = await make_request()
    finished_time = time.time() - start_time
    return jsonify({'message': data, 'execution_time': finished_time})


async def make_request():
    await asyncio.sleep(3)
    return 'a'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
