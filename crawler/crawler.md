# web crawler

# tip
  - xpath = 태그의 경로
  - lxml = parser (구문분석)  
  - requests = html 정보 가져오는 곳
    ```python
    import requests
    res = requests.get("http://naver.com")
    print(res.status_code) # 응답코드 requests.codes.ok
    res.raise_for_status() # 정상이면 코드 실행 아니면 멈춤
    ```
  - 정규식
    ```python
    # doc -> w3c python re
    import re
    p = re.compile("ca.e")
    # . (ca.e): 하나의 문자를 의미 cate , cafe , case (o) | caffe (x)
    # ^ (^de) : 문자열의 시작 desk, destination (o) | fade (x)
    # $ (se$) : 문자열의 끝 case , base (o) | face (x)
    m = p.match("case") # 문자열의 처음부터 일치유
    m = p.search("good care") # 주어진 문자열중에 일치 유무
    m = p.findall("good cafe care") # 일치하는 문자열을 리스트로 반환
    
    print(m.group()) # 일치하는 문자열반환
    print(m.string) # 입력받은 문자열
    print(m.start()) # 일치하는 문자열의 시작 index
    print(m.end()) # 일치하는 문자열의 마지막 index
    print(m.span()) # 일치하는 문자열의 시작/마지막 index
    ```
  - user agent
    ```python
    url = "http://naver.com"
    header = {"User-Agent":""}
    res = requests.get(url,headers=headers)
    ```
    
# beautifulsoup4
  ```python
  from bs4 import BeautifulSoup 
  import requests
  
  res = requests.get("http://naver.com")
  print(res.status_code) 
  res.raise_for_status()
  
  soup = BeautifulSoup(res.text,"lxml")
  
  # class나 다른 유일
  rank = soup.find("태그명",attrs={"class" : "class 값"})
  # class 안의 a태그
  print(rank.a)
  
  # 부모, 형제
  rank.next_sibling
  ```
  