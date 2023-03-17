import cv2

# 카메라 또는 비디오 파일에서 입력 받음
cap = cv2.VideoCapture(0) # 0번 카메라를 사용하거나, 비디오 파일 경로를 입력하세요.

# 작은 픽셀 형식으로 출력하기 위한 리사이즈 크기
pixel_size = 1000

# 현재 프레임과 이전 프레임 초기화
_, frame = cap.read()
prev_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
prev_frame = cv2.resize(prev_frame, (pixel_size, pixel_size))

while True:
    # 프레임을 읽어들임
    ret, frame = cap.read()
    
    # 현재 프레임을 그레이스케일로 변환
    curr_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 현재 프레임을 작은 픽셀 형식으로 리사이즈
    curr_frame = cv2.resize(curr_frame, (pixel_size, pixel_size))
    
    # 현재 프레임과 이전 프레임 사이의 차이 계산
    diff = cv2.absdiff(curr_frame, prev_frame)
    
    # 잔상 출력
    cv2.imshow('residue', diff)
    
    # 이전 프레임을 현재 프레임으로 업데이트
    prev_frame = curr_frame.copy()
    
    # 'q'를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 종료
cap.release()
cv2.destroyAllWindows()
