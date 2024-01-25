# projectPmDust
한국소프트웨어산업협회 -  빅데이터를 활용한 풀스택 개발자 양성과정 / 국제컴퓨터아트학원 천호캠퍼스 세 번째 팀프로젝트

- 프로젝트 주제 : 미세먼지 빅데이터 분석 및 사전 예보 웹사이트 개발 

- 기간: 2023.12.04 ~ 2023.12.29. (4주)

## Team 9교시 : 단아 지현 [선빈](https://github.com/bin2da97).

### skill
- Python, Flask, pandas, tensorflow, Mysql
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


### main work 1 : 미세먼지 데이터 분석 및 Deeplearning
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


### main work 2 : API 연동 및 웹 페이지 데이터 제공
![image](https://github.com/bin2da97/projectPmDust/assets/117819102/73db4c98-da30-4ea6-a1e9-efc5e545e67d)
![image](https://github.com/bin2da97/projectPmDust/assets/117819102/981ec9ed-bac5-4f4f-8022-baf4c3633a54)

- 작업 내용
  - 지도 클릭 시 클릭 지역 실시간 미세먼지 데이터 제공
  - 등급에 따른 색상 변경
  - Flask 서버 미세먼지 API 연동
  - 필요에 맞게 데이터 형태 처리(Pandas 활용)
  - 지도 생성 및 클릭 시 이벤트 구현

 
### main work 3 : 회원가입 & 회원 가입

#### 회원 가입
![image](https://github.com/bin2da97/projectPmDust/assets/117819102/fe80c47d-ee82-4d67-b10e-585658c5221e)
![image](https://github.com/bin2da97/projectPmDust/assets/117819102/879c5620-e35c-46a3-a692-e0bfd94a10c1)

- 작업 내용
  -Form을 활용한 회원가입, 소셜 회원가입
    /signup 엔드 포인트로 POST 요청이 들어오면, 클라이언트에서 전송한 폼 데이터 추출
  - 중복여부 확인, 유효성 검사, 이메일 형식 확인 및 안내
  - 이미지 업로드 시, 해당 아이디로 폴더 생성하여 이미지 저장, DB에 이미지 경로 저장
  - 얼굴 인식 딥러닝 학습을 위해 이미지를 사용하여 KNN 분류 훈련 실행

 #### 로그인
 ![image](https://github.com/bin2da97/projectPmDust/assets/117819102/f73f06e6-a12b-459e-a435-08e7dcc6b2dd)

- 작업 내용
  - Form 활용 로그인, 소셜 로그인 
  - /signin 엔드 포인트로 POST 요청이 들어오면, 클라이언트가 제공한 JSON 데이터를 받아오고 DB에서 조회
  - 로그인 성공 시, 클라이언트에게 성공 메시지와 함께 발급된 토큰을 전달
  - 비밀번호가 일치하지 않거나 아이디가 존재하지 않는 경우 오류 메시지를 반환

#### 얼굴인식 로그인
  - 외장 캠 사용
    
  ![image](https://github.com/bin2da97/projectPmDust/assets/117819102/390f3c3b-1259-4df7-93ef-087a0565733a)
  ![image](https://github.com/bin2da97/projectPmDust/assets/117819102/4e84eda4-e3de-4790-a031-6d7e117daeb9)

- 작업 내용  
  - 얼굴 인식 로그인 버튼 클릭시,  사용자를 식별하고 로그인을 수행 
  - /facelogin 엔드 포인트로 GET 요청이 들어오면, 얼굴 인식을 시작
  - OpenCV와 face_recognition 라이브러리를 사용하여 얼굴을 감지하고 인식
  - 회원가입 시 미리 훈련된 모델을 사용하여 가장 유사한 얼굴 식별
  - 인증 성공 시, 해당 사용자의 정보 데이터베이스에서 조회하고 토큰 생성
  - 인증 실패 하거나 아이디가 존재하지 않는 경우 오류 메시지를 반환




