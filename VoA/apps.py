import pyautogui,time

def screenshot():
    try:
        filename = time.strftime("%Y%m%d-%H%M%S")
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'C:\Users\Natasha\Pictures\Saved Pictures'+ '\\' + filename + '.png')
        output = "OK"
        return  output
    except:
        output = "Error"
        return output