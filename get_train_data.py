import cv2
import tkinter as tk
from tkinter import Button
from PIL import Image, ImageTk
import os

# 创建保存图片的目录
if not os.path.exists('images'):
    os.makedirs('images')

# 拍照函数
def take_snapshot():
    ret, frame = cap.read()
    if ret:
        img_name = f"images/frame_{len(os.listdir('images')) + 1}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"{img_name} saved")

# 更新显示的帧
def update_frame():
    ret, frame = cap.read()
    if ret:
        cv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv_img)
        img_tk = ImageTk.PhotoImage(image=img)
        label.imgtk = img_tk
        label.configure(image=img_tk)
    label.after(10, update_frame)

# 初始化主窗口
root = tk.Tk()
root.title("Camera GUI")

# 创建标签，用于显示摄像头帧
label = tk.Label(root)
label.grid(row=0, column=0, columnspan=2)

# 创建拍照按钮
btn_snapshot = Button(root, text="Snapshot", command=take_snapshot)
btn_snapshot.grid(row=1, column=0)

# 创建退出按钮
btn_exit = Button(root, text="Exit", command=root.destroy)
btn_exit.grid(row=1, column=1)

# 初始化摄像头
cap = cv2.VideoCapture(0)

# 尝试设置摄像头的分辨率
desired_width = 1920    
desired_height = 1080
cap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)

update_frame()

# 运行主循环
root.mainloop()

# 释放摄像头资源
cap.release()
cv2.destroyAllWindows()
