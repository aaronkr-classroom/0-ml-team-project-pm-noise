# Noise / *도로 통행량 기반 소음 정도 시각화*
# [Go to Google Slide](https://docs.google.com/presentation/d/1QlMydYnJ-UwxVdMc6XjU5LuIHG9hgC0fcfOnTGyLvu0/edit?usp=sharing)
🛣️'s <br>
🚌 BUS 🚌 <br>
🏍️ Bike 🏍️ <br>
🚗 Common 🚙 <br>
🚚 Truck 🚚 <br>

💻🤔(road noise calculation) -> Noise Level!
## 팀원 및 역할

- 1945122 최성주 (팀장)
  - 데이터 전처리, 증강
- 2026086 김민찬
  - 여러 모델 테스트
- 2026103 이차원
  - 모델 튜닝
- 2126075 한주영
  - 성능 평가
- 2425404 서상원
  - 최적화

## 프로젝트 명

### 도로 통행량 기반 소음 정도 시각화

### 데이터셋

#### [AI HUB 자동차 차종/연식/번호판 인식용 영상](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=172)

> 상기 데이터셋은 한국지능정보사회진흥원의 사업결과이며<br>
> 해당 데이터 이용을 밝힘

## :fire::fire: 4 Class ver :fire::fire: Current Main
:blue_car: Hatchback, Sedan, SUV, Van <br>
차를 잘 모르는 사람들도 구별하기 힘들어 <br>
모델이 분류하기 어려움 <br>

<img src="https://i0.wp.com/www.proadvisecar.com/wp-content/uploads/2018/05/Three_body_styles_with_pillars_and_boxes-Copy-3.png?w=1041&ssl=1" alt="sedan" width="400"/>
<img src="https://i0.wp.com/www.proadvisecar.com/wp-content/uploads/2018/05/Three_body_styles_with_pillars_and_boxes-Copy-2.png?w=1041&ssl=1" alt="hatchback" width="400"/>
:arrow_down:<br>
**Common**으로 통합

```
Dataset_4_class
├── Test
│   ├──  BUS
│   ├──  Bike
│   ├──  Common
│   └──  Truck
└──  Train
    ├──  BUS
    ├──  Bike
    ├──  Common
    └──  Truck
```

```
class_indices = {'BUS': 0, 'Bike': 1, 'Common': 2, 'Truck': 3}
```

## 8 Class ver
```
Dataset_8_class
├── Test
│   ├──  BUS
│   ├──  Bike
│   ├──  HatchBack
│   ├──  Sedan
│   ├──  SUV
│   ├──  Truck
│   ├──  Truck2
│   └──  Van
└──  Train
    ├──  BUS
    ├──  Bike
    ├──  HatchBack
    ├──  Sedan
    ├──  SUV
    ├──  Truck
    ├──  Truck2
    └──  Van
```

```
class_indices = {'BUS': 0, 'Bike': 1, 'HatchBack': 2, 'SUV': 3, 'Sedan': 4, 'Truck': 5, 'Truck2': 6, 'Van': 7}
```

## **:exclamation::exclamation: 위 순서랑 같아야 주피터 노트북에서 라벨이 맞게 붙습니다 :exclamation::exclamation:**

**정렬 옵션에 따라 BUS / Bike 위치가 바뀔 수 있습니다** <br>
순서가 다르면 class_indices 의 위치를 바꿔주시면 레이블이 맞게 붙습니다

```
.
├── Dataset_4_class
│  ├── Test
│  └── Train
├── Dataset_8_class
│  ├── Test
│  └── Train
├── Jupiter
│  ├── cnn_4_class
│  ├── cnn_8_class
│  ├── DenseNet121
│  ├── EfficientNetB0
│  ├── MobileNet
│  ├── noise_calculater
│  └── ResNet50
├── LICENSE
├── Proposal.md
├── README.md
└── requirements.txt
```

## 선택 이유

시간대 별로 건물 주변의 오토바이, 승용차, 트럭이 지나간 횟수를 세어, 소음 정도를 측정하는 알고리즘을 적용해, 소음이 가장 심한 시간대를 파악하여 소음 문제에서 벗어날 수 있습니다.

## 과정

1. 데이터 전처리 및 증강
2. 여러 모델 탐색 및 테스트
3. 모델 튜닝
4. 성능 평가 후 최적 모델 선정
5. 최적화
6. 프로젝트 발표 자료 제작, 성능 지표, 시각화 자료 등 추가

