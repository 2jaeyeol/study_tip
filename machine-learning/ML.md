# Machine/Deep Learning
<br/><br/><br/>

# 연관
### Andrew Ng's ML class
https://www.coursera.org/ml-003/lecture<br/>
http://holehouse.org/mlclass/

### Convolutional Neural Networks for Visual Recognition
https://cs231n.github.io/

### Tensorflow
https://www.tensorflow.org/<br/>
https://github.com/aymericdamien/tensorflow-examples/<br/>
https://opentutorials.org/module/4966

### sung Kim
http://hunkim.github.io/ml/<br/>
https://github.com/hunkim/DeepLearningZeroToAll/tree/master/tf2

<br/><br/>

# 용어와 개념
## ML
- 프로그램 자체가 데이터를 학습해서 배우는 능력을 갖는 것(프로세스?)

## 학습방법
  - Supervised 
    - 정해져있는 데이터를 갖고 학습하는 것
    - (회귀) regression 
    - (분류) binary classification / multi-label classification
  - Unsupervised
    - 데이터를 보고 스스로 학습하는 것
  - 독립변수(원인) , 종속변수(결과)
## 알고리즘
  - Decision Tree
  - Random Forest
  - KNN
  - SYM
  - Neaural Network(Deep Learning)

# TensorFlow

## 사용
  - colaboratory , jupiter notebook 사용 가능
  
  1. Data Flow graph : Node(operation) + Edge(data array)
<br/>

  - 모델구조(회귀)

```python
  # 1은 컬럼수
  X = tf.keras.layers.Input(shape=[1])
  Y = tf.keras.layers.Dense(1)(X)
  model = tf.keras.models.Model(X,Y)
  # loss 학습의 정도
  # loss = (예측 - 결과)^2 들의 평균 0에 가까울수록 학습이 잘됨 
  model.compile(loss='mse')

  # 모델 학습(FIT) epochs = 반복학습
  model.fit(독립, 종속, epochs = 1000)

  # 모델 이용
  print('Predications: ', model.predict([[15]]))
  # 모델의 수식확인
  model.get_weights()
  # 요약
  model.summury() 
```
  
  - 모델구조(분류)
  ```python
  X = tf.keras.layers.Input(shape=[4])
  # 비율을 찾는 것 sigmoid와 softmax의 차이(activation 활성화함수)
  Y = tf.keras.layers.Dense(3, activation = 'softmax')(X)
  model = tf.keras.models.Model(X,Y)
  model.compile(loss='categorical_crossentropy', metrics = 'accuracy')
  ```

  - 히든 레이어
  ```python
  X = tf.keras.layers.Input(shape=[13])
  H = tf.keras.layers.Dense(5, activation = 'swish')(X)
  
  H = tf.keras.layers.Dense(1)(H)
  model = tf.keras.models.Model(X,Y)
  model.compile(loss='categorical_crossentropy', metrics = 'accuracy')
  ```
  - 학습모델
  ```python
  H = tf.keras.layers.Dense(5)(X)
  H = tf.keras.layers.BatchNormalization()(H)
  H = tf.keras.layer.Activation('swish')(H)
  H = tf.keras.layers.Dense(1)(H)
  model = tf.keras.models.Model(X,Y)
  ```

## image
  - 이미지 불러오기
    ```python
    import matplotlib.pyplot as plt
    import pandas as pd

    (mnist_x, mnist_y), _ = tf.keras.datasets.mnist.load_data()
    print(mnist_x.shape,mnist_y.shape)

    (cifar_x, cifar_y), _ = tf.keras.datasets.cifar10.load_data()
    print(cifar_x.shape,cifar_y.shape)

    plt.imshow(mnist_x[0], cmap='gray')
    plt.show()
    ```
    
- 기본 이미지 학습
  ```python
  # 데이터 준비
  (독립, 종속), _ = tf.keras.datasets.mnist.load_data()
  print(독립.shape , 종속.shape)
  독립 = 독립.reshape(60000,784)
  종속 = pd.get.dummies(종속)
  print(독립.shape , 종속.shape)

  # 모델생성
  X = tf.keras.layers.Input(shape=[784])
  H = tf.keras.layers.Dense(84, activation='swish')(X)
  Y = tf.keras.layers.Dense(10, activation='softmax')(H)
  model = tf.keras.models.Model(X, Y)
  model.compile(loss='categorical_crossentropy', metrics='accuracy')

  # 모델 학습
  model.fit(독립, 종속, epochs=10)

  # 모델을 이용합니다. 
  pred = model.predict(독립[0:5])
  pd.DataFrame(pred).round(2)
  
  ```
- Flatten Layer를 활용한 이미지 학습
  ```python
  # 데이터준비에서
    독립 = 독립.reshape(60000,784) 삭제
  # 모델생성에서 
  H = tf.keras.layers.Flatten()(X) 추가
  ```

- convolution : 특정한 패턴의 특징이 어디서 나타나는지 확인하는 도구
  ```python
  # 모델 생성
  X = tf.keras.layers.Input(shape=[28, 28, 1])
  #필터셋을 3개로 필터셋 사이즈를 5로 
  H = tf.keras.layers.Conv2D(3, kernel_size=5, activation='swish')(X)
  H = tf.keras.layers.Conv2D(6, kernel_size=5, activation='swish')(H)
  H = tf.keras.layers.Flatten()(H)
  H = tf.keras.layers.Dense(84, activation='swish')(H)
  Y = tf.keras.layers.Dense(10, activation='softmax')(H)
  model = tf.keras.models.Model(X, Y)
  model.compile(loss='categorical_crossentropy', metrics='accuracy')
  ```

# Pandas
  ## 데이터 읽어오기
  ```python
  파일경로 = '파일경로'
  변수이름 = pd.read_csv(파일경로)
  # 원핫인코딩 범주형의 데이터를 수치화  
  변수이름 = pd.get_dummies(아이리스)
  # 모양 확인
  print(변수이름.shape)
  # 컬럼이름 출력
  print(변수이름.columns)
  # 변수 나누기
  독립 = 변수이름[['컬럼명']]
  종속 = 변수이름[['컬럼명']]
  # head() 출력 5개
  변수명.head()
  # 데이터타입
  변수명.dtypes()
  # 데이터변경
  아이리스['품종'] = 아이리스['품종'].astype('category')
  # NA값 체크
  변수명.isna().sum()
  # NA값에 꽃잎 폭 평균값 넣어주는 방법
  mean = 아이리스['꽃잎폭'].mean()
  아이리스['꽃잎폭'] = 아이리스['꽃잎폭'].fillna(mean)
  ```

# numpy를 이용한 차원확인
 ```python
    import numpy as np
    d1 = np.array([1,2,3,4,5])
    print(d1.shape)
    #(5,)
    
    d2 = np.array([d1,d1,d1,d1])
    print(d2.shape)
    #(4,5)

 ```




