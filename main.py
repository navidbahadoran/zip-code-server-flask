from flask import Flask
import os
import csv

app = Flask(__name__)


def find_coordinate(zip_code):
    header = ['ZIP', 'LAT', 'LNG']
    with open('zipcode.txt') as csv_file:
        csv_reader = csv.DictReader(csv_file, fieldnames=header)
        for item in csv_reader:
            if item['ZIP'] == str(zip_code):
                return f'Lat:{item["LAT"]}, Long:{item["LNG"]}'
    return 'The zipcode is not in the list'


@app.route('/<zip_code>/')
def get_coordinate(zip_code):
    return find_coordinate(zip_code)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 6738))
    app.run(host='0.0.0.0', port=port)
