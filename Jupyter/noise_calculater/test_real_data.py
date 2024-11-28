import os
import random
from PIL import Image, ImageDraw, ImageFont
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet import preprocess_input
import numpy as np

# 모델 로드
model = load_model('DenseNet121.h5')

# 데이터 경로와 클래스 설정
test_dir = '../../../Dataset_4_class/Test'

index_to_class = [folder for folder in os.listdir(train_dir)
                  if os.path.isdir(os.path.join(train_dir, folder)) and folder != '.ipynb_checkpoints']

# 모델 입력 크기
img_size = (128, 128)  # 모델 입력 크기

# 여백 설정
padding = 20  # 이미지 간 여백 (픽셀 단위)
text_height = 30  # 텍스트 영역 높이

# 랜덤 샘플 테스트
results = []
for class_name in os.listdir(test_dir):
    class_path = os.path.join(test_dir, class_name)
    if not os.path.isdir(class_path):  # 디렉토리인지 확인
        continue

    # 해당 클래스 폴더의 모든 파일 가져오기
    images = [os.path.join(class_path, f) for f in os.listdir(class_path) if f.lower().endswith(('png', 'jpg', 'jpeg'))]

    # 랜덤으로 10개 선택 (이미지가 10개 미만이면 모두 선택)
    sampled_images = random.sample(images, min(10, len(images)))

    # 예측 수행
    for image_path in sampled_images:
        # 이미지 로드 및 전처리
        img = load_img(image_path, target_size=img_size, color_mode='rgb')
        img_array = img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # 예측
        predictions = model.predict(img_array)
        predicted_index = np.argmax(predictions, axis=1)[0]
        predicted_class = index_to_class[predicted_index]

        # 결과 저장
        results.append({
            'image': image_path,
            'predicted_class': predicted_class,
            'true_class': class_name
        })

from noise_calculator import NoiseCalculator
from collections import defaultdict

# decibel_map
decibel_map = {
    "차": 70,
    "버스": 80,
    "트럭": 90,
    "오토바이": 60
}

# NoiseCalculator 객체 생성
noise_calculator = NoiseCalculator(decibel_map)

# 결과 데이터로부터 차량 종류별 개수 집계
detected_vehicles = defaultdict(int)  # 차량별 개수 저장
for result in results:
    predicted_class = result['predicted_class']  # 예측된 클래스 이름
    detected_vehicles[predicted_class] += 1      # 해당 클래스의 개수를 증가

# NoiseCalculator를 사용해 총 소음 계산
total_noise_level = noise_calculator.calculate_total_noise(detected_vehicles)

# 결과 출력
print("차량별 개수:", dict(detected_vehicles))
print(f"총 소음 수준: {total_noise_level:.2f} dB")
