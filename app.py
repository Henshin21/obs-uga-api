from flask import Flask, render_template, request, jsonify
import csv
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()
    currencies = []
    for rate in data[0]['rates']:
        currencies.append((rate['code'], rate['currency']))
    return render_template("index.html", currencies=currencies)

@app.route("/calculate", methods=["POST"])
def calculate():
    currency = request.form["currency"]
    amount = float(request.form["amount"])
    response = requests.get("http://api.nbp.pl/api/exchangerates/rates/C/" + currency + "/?format=json")
    data = response.json()
    rate = data['rates'][0]['ask']
    cost = rate * amount
    return render_template("result.html", currency=currency, amount=amount, cost=cost)

if __name__ == "__main__":
    app.run(debug=True)
