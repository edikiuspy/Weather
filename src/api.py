from flask import Flask, request, jsonify

from Weather.src.air import AirQuality
from Weather.src.controllers import Controller
from Weather.src.repositories import AirRepository

app = Flask(__name__)
class Api:
    def __init__(self):
        self.dto = AirQuality()
        self.repository = AirRepository()
        self.controller = Controller(self.repository, self.dto)


    def get_air_qualities(self):
        return jsonify(self.controller.get_air_quality()),200
    def get_air_quality_by_timestamp(self, timestamp):

        try:
            timestamp = self.dto.validate_timestamp(timestamp)
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        air_quality = self.controller.get_air_quality_by_timestamp(timestamp)
        if air_quality:
            return jsonify(air_quality), 200
        return jsonify({'error': 'Air quality not found'}), 404
airApi=Api()
@app.route('/air', methods=['GET'])
def get_air_qualities():
    return airApi.get_air_qualities()
@app.route('/air/', methods=['POST'])
def add_air_quality():
    try:
        airApi.controller.add_air_quality(request.json)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return '', 201
@app.route('/air/<timestamp>', methods=['GET'])
def get_air_quality_by_timestamp(timestamp):
    return airApi.get_air_quality_by_timestamp(timestamp)
if __name__ == '__main__':
    app.run()