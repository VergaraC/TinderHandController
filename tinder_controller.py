import pyautogui

def like():
    pyautogui.keyUp('right')
    print("like")

def dislike():
    pyautogui.keyUp('left')
    print("dislike")

def superlike():
    pyautogui.press('enter')
    print("superlike")

def next_image():
    pyautogui.press('space')
    print("next image")

def open_profile():
    pyautogui.press('up')
    print("open profile")

def close_profile():
    pyautogui.press('down')
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
    pyautogui.press('esc')
