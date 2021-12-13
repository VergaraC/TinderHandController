import pyautogui


def like():
    pyautogui.keyUp('right')

def dislike():
    pyautogui.keyUp('left')

def superlike():
    pyautogui.keyUp('enter')

def nextImage():
    pyautogui.keyUp('space')

def openProfile():
    pyautogui.keyUp('up')

def closeProfile():
    pyautogui.keyUp('down')
def scrolUp(profileStatus):
    if profileStatus == 0:
        openProfile()
        profileStatus = 1
    pyautogui.scroll(100)
    return profileStatus

def scrolDown(profileStatus):
    if profileStatus == 0:
        openProfile()
        profileStatus = 1
    pyautogui.scroll(-100)
    return profileStatus
nextImage()
