import cv2

# 读取原始图片
img = cv2.imread("all.jpg")
if img is None:
    print("无法读取图像")
    exit()

# 转换为灰度图
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("all_gray.jpg", gray_img)

# 转换为HSV格式
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imwrite("all_hsv.jpg", hsv_img)

# 转换为LAB格式
lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imwrite("all_lab.jpg", lab_img)