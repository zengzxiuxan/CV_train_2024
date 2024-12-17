import cv2

# 打开摄像头
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

while True:
    # 读取一帧图像
    ret, frame = cap.read()
    if not ret:
        print("无法获取帧")
        break

    # 转换为灰度图，方便后续处理（这里假设物料与背景有一定灰度差异，可根据实际情况调整）
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 进行阈值处理，提取物料轮廓，这里简单示例，阈值等参数可能需根据实际调整
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # 查找轮廓
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # 计算外接矩形
        x, y, w, h = cv2.boundingRect(contour)

        # 计算外接矩形的几何中心坐标
        center_x = x + w // 2
        center_y = y + h // 2

        # 获取轮廓颜色（这里以平均颜色为例，也可采用其他策略）
        mean_color = cv2.mean(frame[y:y + h, x:x + w])[:3]
        opposite_color = [255 - int(c) for c in mean_color]

        # 在原图像上绘制相反颜色的轮廓
        cv2.drawContours(frame, [contour], -1, tuple(opposite_color), 2)

        # 在原图像上用相同颜色绘制十字标记几何中心
        cv2.line(frame, (center_x - 5, center_y), (center_x + 5, center_y), tuple(mean_color), 2)
        cv2.line(frame, (center_x, center_y - 5), (center_x, center_y + 5), tuple(mean_color), 2)

    # 显示处理后的图像
    cv2.imshow("Processed Frame", frame)

    # 按下Esc键退出循环
    key = cv2.waitKey(1)
    if key == 27:
        break

# 释放摄像头资源并关闭窗口
cap.release()
cv2.destroyAllWindows()