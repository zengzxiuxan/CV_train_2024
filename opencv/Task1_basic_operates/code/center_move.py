import cv2
import numpy as np

# 打开摄像头，0表示默认摄像头，可根据实际情况选择对应的摄像头编号
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("无法打开摄像头，请检查设备连接及权限设置。")
    exit()

while True:
    # 读取一帧图像
    ret, frame = cap.read()
    if not ret:
        print("读取图像帧失败，可能摄像头出现故障，请检查。")
        break

    # 将图像从BGR颜色空间转换为HSV颜色空间，方便后续进行颜色阈值处理
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 定义要检测的物料颜色范围（以红色为例，在HSV颜色空间中）
    # 注意：红色在HSV中跨越两部分，所以分两段定义范围
    lower_red_1 = np.array([0, 100, 60])
    upper_red_1 = np.array([20, 255, 255])
    lower_red_2 = np.array([160, 100, 60])
    upper_red_2 = np.array([180, 255, 255])

    # 根据定义的颜色范围创建掩膜，提取出对应颜色（红色）的区域
    mask_1 = cv2.inRange(hsv_frame, lower_red_1, upper_red_1)
    mask_2 = cv2.inRange(hsv_frame, lower_red_2, upper_red_2)
    combined_mask = cv2.bitwise_or(mask_1, mask_2)

    # 进行形态学操作（开运算），用于去除噪点、使物料轮廓更清晰
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    processed_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_OPEN, kernel)

    # 查找轮廓，只获取最外层轮廓，并对轮廓进行简化表示
    contours, _ = cv2.findContours(processed_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # 计算外接矩形的坐标及宽高
        x, y, w, h = cv2.boundingRect(contour)

        # 计算外接矩形的面积
        area = w * h

        # 设置面积阈值，根据实际情况调整，这里示例设为1000，小于该面积的框将被过滤掉
        area_threshold = 1000
        if area > area_threshold:
            # 计算外接矩形的几何中心坐标
            center_x = x + w // 2
            center_y = y + h // 2

            # 获取轮廓颜色（这里以平均颜色为例，可按需采用其他策略）
            mean_color = cv2.mean(frame[y:y + h, x:x + w])[:3]
            mean_color = [int(c) for c in mean_color]

            # 计算与轮廓颜色相反的颜色（每个通道值用255减去原通道值）
            opposite_color = [255 - int(c) for c in mean_color]

            # 在原图像上绘制相反颜色的轮廓，线宽设为2
            cv2.drawContours(frame, [contour], -1, tuple(opposite_color), 2)

            # 绘制外接矩形框，颜色与轮廓相同，线宽设为2
            cv2.rectangle(frame, (x, y), (x + w, y + h), tuple(mean_color), 2)

            # 计算十字标记长度，占外接矩形宽高的40%
            half_w = int(w * 0.4 / 2)
            half_h = int(h * 0.4 / 2)

            # 在原图像上用与轮廓相同的颜色绘制十字标记几何中心，线宽设为2
            cv2.line(frame, (center_x - half_w, center_y), (center_x + half_w, center_y), tuple(mean_color), 2)
            cv2.line(frame, (center_x, center_y - half_h), (center_x, center_y + half_h), tuple(mean_color), 2)

    # 显示处理后的图像
    cv2.imshow("Processed Frame", frame)

    # 按下Esc键退出循环，也可根据需求设置其他退出按键
    key = cv2.waitKey(1)
    if key == 27:
        break

# 释放摄像头资源
cap.release()
# 关闭所有已打开的图像显示窗口
cv2.destroyAllWindows()
