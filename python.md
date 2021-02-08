# python

-  변수출력
  ```python
  name = "강아지"
  age = 4
  print("bla bla" + name + "bla bla") 
  print("bla bla" + str(age) + "bla bla")
  ```

- 연산자
  ```python
  print(2**3) # 8
  print(5//3) #몫
  # and -> &
  # or -> |
  print(5>4>3) #true
  ```

- 수 처리
  ```python
  print(abs(-5)) # 절대값
  print(pow(4,n)) # n제곱
  print(max(n1,n2)) # 최대
  print(min(n1,n2)) # 최소
  print(round(4.99)) # 반올림

  from math import *
  print(floor(3.14)) # 내림
  print(ceil(3.14)) # 올림
  print(sqrt(16)) # 제곱근
  
  from random import *
  print(random()) # 0 이상 1미만
  print(randrange(1,46)) #  1이상 46미만
  print(randint(1,45)) # 1이상 45이하
  ```

- 문자열
  ```python
  jumin = "950823-1234567"
  print("연도 : " + jumin[0:2]) # 인덱스 0이상 2미만
  print("월 : " + jumin[2:4]) # 인덱스 2이상 4미만
  print("생년월일 : " + jumin[:6]) # 인덱스 0부터 6미만
  print("뒤 7자리 : " + jumin[7:]) # 인덱스 7부터 끝까지
  print("뒤 7자리 : " + jumin[-7:]) # 뒤부터 7번째에서 끝까지
  ```

- 문자열 처리 함수
  ```python
  python = "Python is Amazing"
  print(python.lower()) # 모두 소문자
  print(python.upper()) # 모두 대문자
  print(python[0].isupper()) # 0번째가 대문자인가?
  print(len(python)) # 문자열 길이 반환
  print(python.replace("Python", "Java")) # Python 을 Java로 변경

  index = python.index("n") # n이 있는 인덱스
  print(index) # 5
  index = python.index("n",index+1) # 처음 찾은 n 다음
  print(index) # 15 

  print(python.find("Java")) # Java를 찾는데 없으면 -1반환
  print(python.index("Java")) # Java를 찾는데 없으면 오류반환
  ```

- 문자열 포맷
  ```python
  print("나는 %s색과 %s색을 좋아합니다." %("파란","빨간"))
  print("나는 {}색과 {}색을 좋아합니다.".format("파란","빨간"))
  print("나는 {0}색과 {1}색을 좋아합니다.".format("파란","빨간"))
  print("나는 {color1}색과 {color2}색을 좋아합니다.".format(color1  = "파란",color2 = "빨간"))
  ```

- 탈출
  ```python
  #/r 커서를 맨앞으로 이동
  print("Red Apple\rPine") # PineApple 
  #/b 하나 삭제
  print("Redd\bApple") # RedApple
  #/t 탭
  print("Red\tApple") # Red   Apple
  ```

- 리스트([])
```python
subway = [00,11,22]
#추가
subway.index(11) #11의 인덱스
subway.append(33) # 맨뒤에 삽입
subway.insert(1,01) # 인덱스 1에 추가 
subway.pop() # 맨 뒤 삭제  
subway.count(00) # 같은값 00 이 몇개 있는지

num = [1,4,5,2,3]
num.sort() # 오름차순 정렬
num.reverse() # sort후 내림차순 정렬
num.clear() # 모두 삭제

list1 = [0,0,0]
list2 = [1,1,1]
list1.extend(list2) # [0,0,0,1,1,1]
```

- 사전({}) dictionary
```python
cabinet = {3 : "유재석" , 100 : "박명수"}
print(cabinet[3]) # 유재석 만약 vlaue가 없으면 프로그램 종료
print(cabinet.get(3)) # 유재석 만약 value가 없으면 none
print(cabinet.get(3,"기본값")) # value가 없으면 기본값 출력
print(key값 in cabinet) # cabinet 안에 key값이 없으면 false

del cabinet[0] # key값 0 인것 삭제
print(cabinet.keys()) # key 값만 출력
print(cabinet.values()) # value 값만 출력 
print(cabinet.items()) # 쌍으로 출력
```

- 튜플 추가 변경 불가(속도는 빠름)
```python
menu = ("돈까스" , "소바")
(name , age , hobby) = ("이오순" , "4" , "먹기")
```

- 세트(집합) 중복x 순서x
```python
my_set = {1,2,3,3,3}
print(my_set) # {1,2,3}

java = {"유재석", "박명수", "하하"}
python = set(["유재석", "정준하"])

#교집합
print(java & python) # 유재석 
print(java.intersection(python)) # 유재석

#합집합
print(jave | python)
print(java.union(python))

#차집합
print(jave - python)
print(java.difference(python))

#값 추가
python.add("김태호")
#값 삭제
java.remove("유재석")
```

- 자료구조의 변경
```python
menu = {"돈까스", "소바"}
menu = list(menu)
menu = tuple(menu)
menu = set(menu)

users = range(1,21) # 1부터 20까지 저장 
users = list(users)

```