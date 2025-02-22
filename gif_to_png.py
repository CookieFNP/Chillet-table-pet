import cv2
import os

# 读取GIF文件
gif_path = r"C:\Users\ASUS\Desktop\look.gif"
cap = cv2.VideoCapture(gif_path)

# 创建保存图片的文件夹
save_folder = r"C:\Users\ASUS\Desktop\lookKUM"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# 逐帧读取并保存为PNG
frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_path = os.path.join(save_folder, f'frame_{frame_count:04d}.png')
    cv2.imwrite(frame_path, frame)
    frame_count += 1
    print(frame_count)
# 释放资源
cap.release()