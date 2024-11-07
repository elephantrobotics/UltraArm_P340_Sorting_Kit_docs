import tkinter as tk
import sys
root = tk.Tk()
root.title("消息框")
# 获取屏幕尺寸
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 400
window_height = 300
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
label = tk.Label(root, text="请将机械臂回零后，检查标定参数，将木块放回码垛区域，重新运行程序")
label.pack(pady=20)
def message():
    root.after(3000, root.destroy)
    root.mainloop()
    print("请将机械臂回零后，检查标定参数，将木块放回码垛区域，重新运行程序") 
    sys.exit()    