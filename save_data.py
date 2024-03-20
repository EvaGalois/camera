import cv2
import os

# 设置视频源（摄像头）
cap = cv2.VideoCapture(0)

# 尝试设置摄像头的分辨率
desired_width = 3840    
desired_height = 2160
cap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)

# 读取并使用实际设置的分辨率
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 定义视频编码器和创建 VideoWriter 对象
out = cv2.VideoWriter('videos/output.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 10, (frame_width, frame_height))
frame_count = 0  # 帧计数器
save_frame_interval = 10  # 每隔10帧保存一次图像

# 创建images和videos文件夹（如果不存在）
if not os.path.exists('videos'):
    os.makedirs('videos')
if not os.path.exists('images'):
    os.makedirs('images')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    # 写入视频
    out.write(frame)

    # 每隔10帧保存一张图像
    if frame_count % save_frame_interval == 0:
        image_name = f'images/frame_{frame_count}.jpg'
        cv2.imwrite(image_name, frame)

    # 显示图像
    cv2.imshow('Frame', frame)

    # 按 'q' 退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()
