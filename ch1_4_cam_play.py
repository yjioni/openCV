import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    while True:
        ret, img = cap.read()
        print(cap.read())
        if ret:
            cv2.imshow('cam', img)
            if cv2.waitKey(1) != -1:
                break
        else:
            print('no frame')
            break
else:
    print('cannot open file')

cap.release()
cv2.destroyAllWindows()