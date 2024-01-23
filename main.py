from flask import Flask
from polygon import RESTClient
import os


POLYGON_KEY = os.environ.get('POLYGON_KEY', 'CANT_GET_KEY')

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/aapl")
def AAPL_data():
    ticker = "AAPL"
    client = RESTClient(api_key=f"{POLYGON_KEY}")
    aggs = []
    for a in client.list_aggs(ticker=ticker, multiplier=1,
                              timespan="minute", from_="2023-01-01",
                              to="2023-06-13", limit=50000):
        aggs.append(a)
    return aggs


if __name__ == "__main__":
    app.run()
