import cv2
import numpy as np

file_name = 'download.jpeg'
image = cv2.imread(file_name)

panel = np.zeros([100,400], np.uint8).astype(np.uint8)
cv2.namedWindow('panel')

def nothing(x):
    pass
#ㄴㅇㄹ
cv2.createTrackbar('FX', 'panel', 1,100, nothing)
cv2.createTrackbar('FY', 'panel', 1,100, nothing)

return_name = file_name.replace('.','_pixel.')

while True:
    
    
    fx = cv2.getTrackbarPos('FX', 'panel') / 100
    fy = cv2.getTrackbarPos('FY', 'panel') / 100

    pixel = cv2.resize(image, dsize=None, fx=fx, fy=fy, interpolation=cv2.INTER_NEAREST)
    pixel = cv2.resize(pixel, dsize=(int(image.shape[1]*1),int(image.shape[0]*1)), interpolation=cv2.INTER_NEAREST)
    
    cv2.imshow('image', image)
    cv2.imshow('pixel', pixel)
    cv2.imshow('panel', panel)
    
    if cv2.waitKey(1) == ord('s'):
        cv2.imwrite(return_name, pixel)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
