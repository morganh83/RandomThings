import pyautogui, time

time.sleep(10)
pyautogui.typewrite("m")

def countdown(t):    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    pyautogui.typewrite("m")
  
# input time in seconds
t = "600"

while True:
    countdown(int(t))
