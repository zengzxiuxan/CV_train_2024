import cv2
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("鼠标点击位置坐标: (%d, %d)" % (x, y))
img = cv2.imread("all.jpg")
if img is None:
    print("无法读取图像")
else:
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", mouse_callback)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()