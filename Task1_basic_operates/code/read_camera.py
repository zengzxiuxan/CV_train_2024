import cv2
cap = cv2.VideoCapture(0)  # 打开默认摄像头，0表示默认设备
if not cap.isOpened():
    print("无法打开摄像头")
    exit()
ret, frame = cap.read()  # 读取一帧画面
if not ret:
    print("无法获取帧")
    exit()
# 保存截取的帧为图像文件（可选操作）
cv2.imwrite("all.jpg", frame)
print("已成功截取一帧画面并保存为all.jpg")
cap.release()