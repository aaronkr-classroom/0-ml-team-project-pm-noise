import math
import random
from collections import defaultdict

class NoiseCalculator:
    def __init__(self, decibel_map):
        """
        소음 계산기 초기화.

        Parameters:
            decibel_map (dict): {"차의 종류": 해당 차의 평균 데시벨} 형태의 딕셔너리.
        """
        self.decibel_map = decibel_map

    def generate_vehicle_data(self, duration_seconds=24 * 3600):
        """
        랜덤 차량 데이터를 생성하여 시간 단위로 묶는 함수.

        Parameters:
            duration_seconds (int): 총 데이터 생성 시간(초 단위).

        Returns:
            list: 시간 단위로 묶인 차량 데이터의 리스트.
        """
        vehicles = list(self.decibel_map.keys())
        data_per_second = []  # 초 단위 데이터를 저장할 리스트

        for _ in range(duration_seconds):
            second_data = {
                vehicle: random.randint(100, 1000) for vehicle in vehicles
            }
            data_per_second.append(second_data)

        # 시간 단위로 데이터를 묶음
        hourly_data = []
        for i in range(0, len(data_per_second), 3600):
            hour_data = defaultdict(int)
            for second_data in data_per_second[i:i + 3600]:
                for vehicle, count in second_data.items():
                    hour_data[vehicle] += count
            hourly_data.append(dict(hour_data))

        return hourly_data

    def calculate_total_noise(self, detected_vehicles):
        """
        총 소음 수준(dB)을 계산하는 함수.

        Parameters:
            detected_vehicles (dict): {"차의 종류": 해당 차의 개수} 형태의 딕셔너리.

        Returns:
            float: 합성된 최종 소음 레벨 (dB).
        """
        total_power = 0
        for vehicle_type, count in detected_vehicles.items():
            if vehicle_type in self.decibel_map:
                average_decibel = self.decibel_map[vehicle_type]
                total_power += count * (10 ** (average_decibel / 10))
        if total_power > 0:
            return 10 * math.log10(total_power)
        return 0
