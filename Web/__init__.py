# @Time  : 2019/6/5 0005 10:14
# @Author: LYX
# @File  : __init__.py

from flask import Flask, request, render_template

app = Flask(__name__)

from Astar.star import QueryRoute
from Models.route import Route

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")  # homepage.html在templates文件夹下


@app.route('/query_route', methods=['GET', 'POST'])
def query_route():
    start_where = request.args.get("start_where")
    arrive_where = request.args.get("arrive_where")
    start_where_city = request.args.get("start_where_city")
    arrive_where_city = request.args.get("arrive_where_city")
    print(start_where)
    start = Route(start_where, start_where_city)
    target = Route(arrive_where, arrive_where_city)
    timestamp_start = ("2019-05-30 00:04:59")
    timestamp_end = ("2019-05-31 20:05:00")
    route = QueryRoute(start, target, timestamp_start, timestamp_end)
    result = route.search()
    return result


if __name__ == '__main__':
    app.run()
