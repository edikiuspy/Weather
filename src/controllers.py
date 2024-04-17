from Weather.src.repositories import AirRepository
from Weather.src.air import AirQuality

class Controller:
    def __init__(self,repository: AirRepository,dto: AirQuality):
        self.repository = repository
        self.dto=dto

    def add_air_quality(self, air_data):
        self.dto.add_data(air_data)
        data=self.dto.get_data()
        if None in data:
            raise ValueError('Data is missing')
        self.repository.add_air_quality(self.dto)

    def get_air_quality(self):
        return self.repository.get_air_quality()

    def get_air_quality_by_timestamp(self, timestamp):
        air_quality = self.repository.get_air_quality()
        for aq in air_quality:
            if aq['timestamp'] == timestamp:
                return aq
        return None