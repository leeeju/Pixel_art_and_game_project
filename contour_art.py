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