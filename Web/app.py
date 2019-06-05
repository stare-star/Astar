# @Time  : 2019/6/5 0005 10:14
# @Author: LYX
# @File  : app.py

from flask import Flask, request

from Astar.star import QueryRoute
from Models.route import Route

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/query_route', methods=['GET', 'POST'])
def query_route():
    start_where = request.args.get("start_where")
    arrive_where = request.args.get("arrive_where")
    start_where_city = request.args.get("start_where_city")
    arrive_where_city = request.args.get("arrive_where_city")
    print(start_where)
    start = Route(start_where, start_where_city)
    target = Route(arrive_where, arrive_where_city)
    timestamp_start = 20190529
    timestamp_end = 20190530
    route = QueryRoute(start, target, timestamp_start, timestamp_end)
    result = route.search()
    return result


if __name__ == '__main__':
    app.run()
