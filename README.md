# Pixel_art_and_game_project

### 프로젝트기간 : 2023. 02. 01 ~ 2023. 진행중

환경구성 : Ubuntu22.04, VScode

사용기술 : Qt5, Open_CV, python

#### 팀원 : 이주현
  
  - 연구기록 YouTube -- > https://www.youtube.com/watch?v=tAKOi-Y7-uI
  
  ![github contribution grid snake animation](https://raw.githubusercontent.com/borongyuan/borongyuan/output/github-contribution-grid-snake.svg)
##  프로젝트 목적
###  Ⅰ배경 

Qt5와 Open_CV기초 숙달 및 Object Detection, Line tracking기술의 Basic기술 습득을 위한 toy project 진행


###  Ⅱ성과 (사진첨부&영상첨부)

![KakaoTalk_20230313_205153991](https://user-images.githubusercontent.com/84003327/224695583-de78c9ae-b51a-4ef4-a656-8111dbae44f2.jpg)

```
//! contour_art.py

import cv2

# 카메라 연결
cap = cv2.VideoCapture(0)

while True:
    # 영상 프레임 받아오기
    ret, frame = cap.read()
    
    # 윤곽선 추출
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, 0)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # 윤곽선을 픽셀 형식으로 출력
    pixel_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.drawContours(pixel_img, contours, -1, (255, 255, 255), thickness=2)
    cv2.imshow('contour', pixel_img)
    
    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 카메라 해제
cap.release()
cv2.destroyAllWindows()
```



# Galaga_Wars_game

|file name|Language|project|description|
|------|------|-----|-----|  
|Galaga_Wars.py|python|Pixel|Game|

<img width="300" alt="화면 캡처 2023-03-13 233349" src="https://user-images.githubusercontent.com/84003327/224745028-809b1c0e-6edb-4bf9-9243-681bac68f0b6.png">



