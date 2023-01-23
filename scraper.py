import requests
import csv


response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

with open('currency_rates.csv', mode='w') as currency_file:
    fieldnames = ['currency', 'code', 'bid', 'ask']
    writer = csv.DictWriter(currency_file, fieldnames=fieldnames)
    writer.writeheader()
    for rate in data[0]['rates']:
        writer.writerow({'currency': rate['currency'], 'code': rate['code'], 'bid': rate['bid'], 'ask': rate['ask']})
