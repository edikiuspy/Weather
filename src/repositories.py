from Weather.src.air import AirQuality


class AirRepository:
    def __init__(self):
        self.air_qualities: list[AirQuality] = []
    def add_air_quality(self, air_quality: AirQuality):

        self.air_qualities.append(air_quality.get_data())
    def get_air_quality(self):
        return self.air_qualities