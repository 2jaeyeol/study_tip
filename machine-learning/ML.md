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

# Pandas
  ## 데이터 읽어오기
  ```python
  파일경로 = '파일경로'
  변수이름 = pd.read_csv(파일경로)
  
  # 모양 확인
  print(변수이름.shape)
  # 컬럼이름 출력
  print(변수이름.columns)
  # 변수 나누기
  독립 = 변수이름[['컬럼명']]
  종속 = 변수이름[['컬럼명']]
  # head() 출력 5개
  변수명.head()
  ```




