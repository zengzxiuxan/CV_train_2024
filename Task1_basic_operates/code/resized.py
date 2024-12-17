import cv2
# 读取原始图片
original_img = cv2.imread("all.jpg")
original_height, original_width, _ = original_img.shape
# 假设已经截取了图片，这里读取截取的图片
cropped_img = cv2.imread("Phone.jpg")
cropped_height, cropped_width, _ = cropped_img.shape
width_ratio = original_width / cropped_width
height_ratio = original_height / cropped_height
resized_img = cv2.resize(cropped_img, (original_width, original_height))
resized_height, resized_width, _ = resized_img.shape
assert resized_height == original_height and resized_width == original_width
cv2.imshow("phone_resized.jpg", resized_img)
cv2.imwrite("phone_resized.jpg",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()