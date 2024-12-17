import cv2
# 读取图像
img = cv2.imread("all.jpg")
if img is None:
    print("无法读取图像")
else:
    # 定义截取区域的坐标和大小
    x = 270  # 截取区域左上角x坐标
    y = 194  # 截取区域左上角y坐标
    width = 70  # 截取区域的宽度
    height = 140# 截取区域的高度
    cropped_img = img[y:y + height, x:x + width]
    # 显示截取后的图像
    cv2.imshow("Phone.jpg", cropped_img)
    cv2.imwrite("Phone.jpg",cropped_img)
    cv2.waitKey(0);
    cv2.destroyAllWindows()
