import pyautogui

def like():
    pyautogui.keyUp('right')
    print("like")

def dislike():
    pyautogui.keyUp('left')
    print("dislike")

def superlike():
    pyautogui.keyUp('enter')
    print("superlike")

def next_image():
    pyautogui.keyUp('space')
    print("next image")

def open_profile():
    pyautogui.keyUp('up')
    print("open profile")

def close_profile():
    pyautogui.keyUp('down')
    print("close profile")
def scroll_up(profileStatus):
    if profileStatus == 0:
        openProfile()
        profileStatus = 1
    pyautogui.scroll(100)
    print("scroll up")
    return profileStatus

def scroll_down(profileStatus):
    if profileStatus == 0:
        openProfile()
        profileStatus = 1
    pyautogui.scroll(-100)
    print("scroll down")
    return profileStatus

def close_window():
    print("close window")
    pyautogui.keyUp('esc')
