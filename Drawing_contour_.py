import cv2

# 카메라 캡처 객체 생성
cap = cv2.VideoCapture(0)

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    # 이미지를 그레이스케일로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 이진화
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Contour 추출
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Contour 그리기
    output = cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

    # 픽셀 형식으로 출력
    cv2.imshow('output', output)

    # q 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 메모리 해제
cap.release()
cv2.destroyAllWindows()
