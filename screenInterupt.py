import tkinter as tk
from tkinter import scrolledtext
import pyautogui
import time

def stop_script():
    global running
    running = False

def update_log(log_text):
    log.config(state=tk.NORMAL)
    log.insert(tk.END, log_text)
    log.see(tk.END)  # Scrolls to the end of the log
    log.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Screen Interrupt")

log = scrolledtext.ScrolledText(root, width=50, height=10, state=tk.DISABLED)
log.pack()

stop_button = tk.Button(root, text="Stop", command=stop_script)
stop_button.pack()

running = True

try:
    while running:
        for i in range(0, 240):
            if i > 59:
                log_text = f"Screen interrupt running since {i // 60} hour {i % 60} minutes.....\nTo stop press Ctrl+C twice.\n"
            else:
                log_text = f"Screen interrupt running since {i} minutes.....\nTo stop press Ctrl+C twice.\n"

            update_log(log_text)

            if i % 2 == 0:
                pyautogui.moveTo(1000, i * 10)
                pyautogui.press('shift')
            time.sleep(60)

except KeyboardInterrupt:
    pass

root.destroy()

'''
import pyautogui
import time

while True:
    for i in range(0,240):
        if i>59:
            print("screen inturrupt running since "+ str(i//60) +" hour "+str(i%60) +" minutes.....\nTo stop press Ctrl+C twice.")
        else:
            print("screen inturrupt running since "+ str(i) +" minutes.....\nTo stop press Ctrl+C twice.")
        if i%2==0:
            pyautogui.moveTo(1000,i*10)
            pyautogui.press('shift')
        time.sleep(60)

'''