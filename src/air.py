from pydantic import BaseModel, field_validator
from typing import Optional,Union
from datetime import datetime
class AirQuality(BaseModel):
    _timestamp: Optional[str]
    _air_quality_index_US: Optional[int]
    _air_quality_index_CN: Optional[int]
    _main_pollutant_US: Optional[str]
    _main_pollutant_CN: Optional[str]
    _temperature: Optional[int]
    _atmospheric_pressure: Optional[int]
    _humidity: Optional[int]
    _wind_speed: Optional[int]
    _wind_direction: Optional[int]
    @classmethod
    @field_validator('_timestamp')
    def validate_timestamp(cls, value):
        if not value:
            raise ValueError('Timestamp is required')
        return value
    @classmethod
    @field_validator('air_quality_index_US', 'air_quality_index_CN')
    def validate_air_quality_index_US(cls, value):
        if value is not None and value < 0:
            raise ValueError('Air quality index must be greater than 0')
        return value
    @classmethod
    @field_validator('temperature')
    def validate_temperature(cls, value):
        if value is not None and value < -50:
            raise ValueError('Temperature must be greater than -50')
        return value
    def add_data(self, data: dict[str, Optional[dict[str, Optional[Union[float,datetime]]]]]):
        pollution = data.get('pollution',{})
        weather = data.get('weather',{})
        self._timestamp = pollution.get('ts')
        self._air_quality_index_US = pollution.get('aqius')
        self._air_quality_index_CN = pollution.get('aqicn')
        self._main_pollutant_US = pollution.get('mainus')
        self._main_pollutant_CN = pollution.get('maincn')
        self._temperature = weather.get('tp')
        self._atmospheric_pressure = weather.get('pr')
        self._humidity = weather.get('hu')
        self._wind_speed = weather.get('ws')
        self._wind_direction = weather.get('wd')
    def get_data(self):
        return {
            'timestamp': self._timestamp,
            'air_quality_index_US': self._air_quality_index_US,
            'air_quality_index_CN': self._air_quality_index_CN,
            'main_pollutant_US': self._main_pollutant_US,
            'main_pollutant_CN': self._main_pollutant_CN,
            'temperature': self._temperature,
            'atmospheric_pressure': self._atmospheric_pressure,
            'humidity': self._humidity,
            'wind_speed': self._wind_speed,
            'wind_direction': self._wind_direction
        }
