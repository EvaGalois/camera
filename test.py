import cv2
import time

# 初始化摄像头
cap = cv2.VideoCapture(0)

# 检查摄像头是否已成功开启
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

# 计算帧率
frame_count = 0
start_time = time.time()

while True:
    # 捕获摄像头的一帧
    ret, frame = cap.read()

    # 如果正确读取帧，增加帧计数
    if ret:
        frame_count += 1
    else:
        print("无法读取摄像头画面")
        break

    # 显示结果帧
    cv2.imshow('Camera', frame)

    # 按 'q' 退出循环
    if cv2.waitKey(1) == ord('q'):
        break

# 计算总时间
end_time = time.time()
total_time = end_time - start_time

# 计算帧率
fps = frame_count / total_time

print(f"捕获的帧数: {frame_count}")
print(f"总时间: {total_time} 秒")
print(f"平均帧率: {fps} FPS")

# 释放摄像头
cap.release()
cv2.destroyAllWindows()
fps
