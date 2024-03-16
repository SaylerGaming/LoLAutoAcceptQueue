import cv2
import pyautogui
import os
from time import sleep, time
import requests
from mss import mss
from threading import Thread

def createScreenshot():
    with mss() as sct:
        sct.shot(output="screenshot.png")
    screenshotImg = cv2.imread('./screenshot.png', cv2.IMREAD_GRAYSCALE)
    os.remove('screenshot.png')
    return screenshotImg

def acceptQueue(x, y) -> None:
    currentX, currentY = pyautogui.position()
    pyautogui.moveTo(x, y, duration = 0.1)
    pyautogui.click()
    pyautogui.moveTo(currentX, currentY, duration = 0.1)

def setWindowStatus(window=None):
    sleep(1)
    global currentTime
    global maxValStr
    global isDoneQueing
    while not isDoneQueing:
        print(f'{currentTime}, {maxValStr}')
        if window:
            window.setStatusQueue(f'{currentTime}, {maxValStr}')

        arr = [int(i) for i in  currentTime.split(':')]
        arr[1] += 1
        if(arr[1] == 60):
            arr[0] += 1
            arr[1] -= 60
        currentTime = f'{arr[0]}:{'0' if arr[1] < 10 else ''}{arr[1]}'

        sleep(1)

def findQueue(buttonImg, weight, height, inQueueImg, sleepTime, window):
    screenshotImg = createScreenshot()
    result = cv2.matchTemplate(screenshotImg, buttonImg, cv2.TM_CCOEFF_NORMED)
    _, maxVal, _, maxLoc = cv2.minMaxLoc(result)
    global maxValStr
    maxValStr = str(int(round(maxVal, 2)*100))+'%'
    

    if maxVal >= float(window.config.queueSencitivity):
        acceptQueue(maxLoc[0] + weight/2, maxLoc[1] + height/2)
        if(isComlete(inQueueImg, sleepTime, window)):
            return True
        return False
    else:
        sleep(sleepTime)
        return False

def isComlete(inQueueImg, sleepTime, window) -> bool:
    timeRemain = 12
    global maxValStr
    while timeRemain > 0:
        screenshotImg = createScreenshot()
        result = cv2.matchTemplate(screenshotImg, inQueueImg, cv2.TM_CCOEFF_NORMED)
        _, maxVal, _, _ = cv2.minMaxLoc(result)
        maxValStr = str(int(round(maxVal, 2)*100))+'%'
        print(f'Игра найдена: {maxValStr}')
        
        if maxVal >= float(window.config.inQueueSensitivity):
            sleep(sleepTime)
        else:
            return True
        timeRemain -= sleepTime
    return False

def main(window = None) -> None:
    buttonImg = cv2.imread('./src/acceptQueue.png', cv2.IMREAD_GRAYSCALE)
    weight = buttonImg.shape[1]
    height = buttonImg.shape[0]

    inQueueImg = cv2.imread('./src/inQueue.png', cv2.IMREAD_GRAYSCALE)

    sleepTime = 3

    isDone = False

    global currentTime
    currentTime = '0:01'

    global isDoneQueing
    isDoneQueing = False

    Thread(target=lambda: setWindowStatus(window), daemon=True).start()


    while not isDone:
        isDone = findQueue(buttonImg, weight, height, inQueueImg, sleepTime, window)

    isDoneQueing = True
    if window.config.chatId and window.config.writableToChat:
        requests.get('https://api.telegram.org/bot6736595463:AAHB4szAPZfjbmkTteu73n3aHj1RT1t1dVg/sendMessage?chat_id='+window.config.chatId+'&text=Игра найдена!')

if __name__ == '__main__':
    main()