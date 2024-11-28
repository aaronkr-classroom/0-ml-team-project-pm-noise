"""
frame마다 탐지되는 차량들에 대해서 소음 합성 연산을 합니다.
3600(1시간) frame마다 평균 데시벨 구하고, 00시~24시 그래프를 그립니다.
"""


import matplotlib.pyplot as plt
from noise_calculator import NoiseCalculator

# 데시벨 매핑
decibel_map = {
    "truck": 85,
    "bus": 80,
    "car": 65,
    "motorcycle": 90
}

# NoiseCalculator 초기화
calculator = NoiseCalculator(decibel_map)

# 24시간 분량의 데이터 생성
detected_vehicles_per_hour = calculator.generate_vehicle_data(duration_seconds=24 * 3600)

# 시간별 평균 데시벨 계산
average_decibels_per_hour = []
for vehicles in detected_vehicles_per_hour:
    total_noise = calculator.calculate_total_noise(vehicles)
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
