# ANACONDA

# 사용법
  - 되도록 base 환경 말고 환경을 하나 더 만들어서 할것
  ## 명령어
  - 작업환경 보기 : conda info --envs
  - 작업환경 생성 : conda create -n 작업환경명 anaconda
  - 작업환경 사용 : conda activate 작업환경명
  - 작업환경 종료 : conda deactive
  - 작업환경 삭제 : conda remove - n 작업환경명 -all
  - 설치 패키지 확인 : conda list 
  - 패키지 조회 : conda search 패키지
    - ex) conda search python 설치 가능한 python 목록이 나옴
  - 패키지 설치 : conda install 패키지명=버전
<br/></br>

# VSC 가상환경 
  1. Python: Select Interpreter (command + shift + p)
  2. ~/opt/anaconda3/env/tensor/bin/python3.7 설정 후 실행
