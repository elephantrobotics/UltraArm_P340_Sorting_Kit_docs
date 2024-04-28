import tkinter as tk
import sys
root = tk.Tk()
root.title("message box")
# Get screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 400
window_height = 300
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
label = tk.Label(root, text="Please return the robotic arm to zero, check the calibration parameters, place the wooden block back in the stacking area, and run the program again")
label.pack(pady=20)
def message():
    root.after(3000, root.destroy)
    root.mainloop()
    print("Please return the robotic arm to zero, check the calibration parameters, place the wooden block back in the stacking area, and run the program again") 
    sys.exit()    