
import cv2

def init_video():
    vc1 = cv2.VideoCapture(3)
    vc2 = cv2.VideoCapture(0)

    if vc1.isOpened() and vc2.isOpened():
        rval1, frame1 = vc1.read()
        rval2, frame2 = vc2.read()
    else:
        rval1 = False
        rval2 = False
        frame1 = None
        frame2 = None

    return vc1, vc2, rval1, rval2, frame1, frame2


if __name__ == "__main__":
    vc1, vc2, rval1, rval2, frame1, frame2 = init_video()
    h1, w1 = frame1.shape[:2]
    stereo = cv2.StereoBM_create()
    

    num = 1
    num1 = 1
    num2 = 1
    num3 = 1
    num4 = 1

    while rval1 and rval2:
        stereo.setNumDisparities(16*num)
        stereo.setMinDisparity(num1)
        stereo.setBlockSize(5+2*num2)
        stereo.setSpeckleRange(num3)
        stereo.setSpeckleWindowSize(num4)

        rval1, frame1 = vc1.read()
        rval2, frame2 = vc2.read()

        gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        disparity = stereo.compute(gray1, gray2)
        depth = disparity/2048

        cv2.imshow("cam1", frame1)
        cv2.imshow("cam2", frame2)
        cv2.imshow("depth", depth)

        key = cv2.waitKey(20)
        if key == 27:
            break
        elif key == ord('w'):
            num += 1
            print('numDisparities' + str(16*num))
        elif key == ord('s'):
            num -= 1
            print('numDisparities' + str(16*num))
        elif key == ord('e'):
            num1 += 1
            print('minDisparities' + str(num1))
        elif key == ord('d'):
            num1 -= 1
            print('minDisparities' + str(num1))
        elif key == ord('r'):
            num2 += 1
            print('blockSize' + str(5+2*num2))
        elif key == ord('f'):
            num2 -= 1
            print('blockSize' + str(5+2*num2))
        elif key == ord('t'):
            num3 += 1
            print('speckleRange' + str(5+2*num3))
        elif key == ord('g'):
            num3 -= 1
            print('speckleRange' + str(5+2*num3))
        elif key == ord('y'):
            num4 += 1
            print('speckleWindowSize' + str(5+2*num4))
        elif key == ord('h'):
            num4 -= 1
            print('speckleWindowSize' + str(5+2*num4))


    cv2.destroyAllWindows()