# projectPmDust
한국소프트웨어산업협회 -  빅데이터를 활용한 풀스택 개발자 양성과정 / 국제컴퓨터아트학원 천호캠퍼스 세 번째 팀프로젝트

- 프로젝트 주제 : 미세먼지 빅데이터 분석 및 사전 예보 웹사이트 개발 

- 기간: 2023.12.04 ~ 2023.12.29. (4주)

## Team 9교시 : 단아 지현 [선빈](https://github.com/bin2da97).

### skill
- Python, Flask, tensorflow, Mysql
- Javascript, React , JQuery, Chart.js, D3.js
- Vscode, pycharm, jupyter notebook


### 주요역할 및 담당: 
- Mysql 데이터 베이스 구축
- Open api 활용하여 실시간 데이터를 웹페이지에 시각화(지도 구현), 챗봇 구현
- 미세먼지 데이터 활용하여 딥러닝을 통한 예측 시스템 개발
- 로그인 기능, face_recognition 라이브러리 활용 얼굴인식 로그인 기능

## 성과 및 느낀점
- 학습 커리큘럼에 없는 React 언어를 새롭게 시도해 프로젝트를 완성
- 서버에서 다양한 정보를 수집, 처리하고 웹 프론트엔드에서 구현 
- Pandas DataFrame을 활용한 데이터 변환 숙련도 증가
- Flask 서버와 React 통신 방식에 대한 이해
- Open api 통신 방식, rest api에 대한 이해
- 딥러닝 모델 직접 구현을 통해 수업 시간과 인공지능 수학 스터디에서 배웠던 선형대수 ,미적분, 선형회귀,Logistic Regression , 신경망, 경사하강법에  대한  심층적 이해
- 미세먼지 데이터 활용하여 딥러닝을 통한 예측 시스템 개발에 대한 부족함과 연구 필요성을 느낌

## 프로젝트 요약

# main page
![image](https://github.com/bin2da97/projectPmDust/assets/117819102/5f0944de-c7e3-4f3e-ba3a-b2208de36d03)

# main work1 미세먼지 데이터 분석 및 Deeplearning
  - 4년의 기상정보 데이터 수집 : 분석시 계절에 따른 미세먼지 동향을 볼 수 있었다.
  - 데이터 전처리
    -불필요한 column 삭제
    -nan 값과, 미세먼지가 400이 넘어가는 이상치는 제거
    - x,y 데이터 분리 (미세먼지는 종속 변수 그 외는 독립 변수)
    - 정규화
    - train, test 데이터 분리
  - RNN 모델
    - CONVID 레이어는 1차원 합성곱(CONVOLUTION)을 수행 입력 데이터를 SEQUENCE_X(시퀀스 길이)와 FEATURE_K(특성의 수)에 맞게 처리하여 데이터의 지역적 특징을 추출
    - LSTM(LONG SHORT-TERM MEMORY) 레이어는 순환 신경망(RNN)는 이전 정보를 유지하면서 시퀀스 데이터의 패턴 파악
    - DENSE 레이어(16개 뉴런)는 16개의 뉴런을 가진 밀집층으로 이전 레이어의 출력을 입력받아 비선형 함수를 사용하여 입력 데이터의 패턴 학습
    - DENSE 레이어(SEQUENCE_Y 개의 뉴런)는 시퀀스의 각 위치에서 예측해야 하는 출력 값의 개수에 맞게 뉴런을 가진 밀집층으로 모델이 시퀀스의 각 요소에 대한 출력을 생성하도록 도우며, 컨볼루션 신경망(CNN)과 재귀 신경망(RNN)의 조합으로 시퀀스 데이터에서 패턴을 학습하여 예측하고자 하는 결과를 생성하는데 사용
  - model compile & train
  - train data

    ![image](https://github.com/bin2da97/projectPmDust/assets/117819102/60a83609-d164-4077-972c-ae60d3ddbb65)

  - validation data

    ![image](https://github.com/bin2da97/projectPmDust/assets/117819102/6a7c1a7c-5028-46cb-aa87-69fa91b15cd4)

  - predict data

    ![image](https://github.com/bin2da97/projectPmDust/assets/117819102/2922cd05-a798-4c47-b709-b16956ae4e97)






