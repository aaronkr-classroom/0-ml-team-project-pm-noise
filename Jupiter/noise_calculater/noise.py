import math
import random
from collections import defaultdict
import matplotlib.pyplot as plt

# 데시벨 매핑
decibel_map = {
    "truck": 85,
    "bus": 80,
    "car": 65,
    "motorcycle": 90
}

# 차량 데이터 생성 함수
def generate_vehicle_data(duration_seconds=24 * 3600):
    """
    랜덤 차량 데이터를 생성하여 시간 단위로 묶는 함수.

    Parameters:
        duration_seconds (int): 총 데이터 생성 시간(초 단위).

    Returns:
        list: 시간 단위로 묶인 차량 데이터의 리스트.
    """
    vehicles = ["truck", "bus", "car", "motorcycle"]
    data_per_second = []  # 초 단위 데이터를 저장할 리스트

    # 초 단위로 데이터 생성
    for _ in range(duration_seconds):
        second_data = {
            vehicle: random.randint(100, 1000) for vehicle in vehicles  # 각 차량별 랜덤 개수
        }
        data_per_second.append(second_data)

    # 시간 단위로 데이터를 묶음
    hourly_data = []
    for i in range(0, len(data_per_second), 3600):  # 3600초(1시간) 단위로 묶기
        hour_data = defaultdict(int)
        for second_data in data_per_second[i:i + 3600]:  # 1시간 동안의 데이터 합산
            for vehicle, count in second_data.items():
                hour_data[vehicle] += count
        hourly_data.append(dict(hour_data))

    return hourly_data

# 소음 계산 함수
def calculate_total_noise(detected_vehicles, decibel_map):
    """
    총 소음 수준(dB)을 계산하는 함수.

    Parameters:
        detected_vehicles (dict): {"차의 종류": 해당 차의 개수} 형태의 딕셔너리.
        decibel_map (dict): {"차의 종류": 해당 차의 평균 데시벨} 형태의 딕셔너리.

    Returns:
        float: 합성된 최종 소음 레벨 (dB).
    """
    total_power = 0
    for vehicle_type, count in detected_vehicles.items():
        if vehicle_type in decibel_map:
            average_decibel = decibel_map[vehicle_type]
            total_power += count * (10 ** (average_decibel / 10))
    if total_power > 0:
        return 10 * math.log10(total_power)
    return 0

# 24시간 분량의 데이터 생성
detected_vehicles_per_hour = generate_vehicle_data(duration_seconds=24 * 3600)

# 시간별 평균 데시벨 계산
average_decibels_per_hour = []
for vehicles in detected_vehicles_per_hour:
    total_noise = calculate_total_noise(vehicles, decibel_map)
    average_decibels_per_hour.append(total_noise)

# 데이터 시각화
plt.figure(figsize=(14, 7))
plt.plot(range(1, len(average_decibels_per_hour) + 1), average_decibels_per_hour, marker='o', linestyle='-', label='Average decibel')
plt.title("Average decibel changes over 24 hours", fontsize=16)
plt.xlabel("Hours (in hours)", fontsize=14)
plt.ylabel("Average decibels (dB)", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(range(1, len(average_decibels_per_hour) + 1), fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)
plt.show()

# 결과 출력
for hour, avg_db in enumerate(average_decibels_per_hour, start=1):
    print(f"Hour {hour}: {avg_db:.2f} dB")
