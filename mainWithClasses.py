import cv2
import pyautogui
import os
from time import sleep, time
import requests
from mss import mss
from threading import Thread

class QueueFinder():
    def __init__(self):
        self.isDone = False
    def createScreenshot(self):
        with mss() as sct:
            sct.shot(output="screenshot.png")
        screenshotImg = cv2.imread('./screenshot.png', cv2.IMREAD_GRAYSCALE)
        os.remove('screenshot.png')
        return screenshotImg

    def acceptQueue(self, x, y) -> None:
        currentX, currentY = pyautogui.position()
        pyautogui.moveTo(x, y, duration = 0.1)
        pyautogui.click()
        pyautogui.moveTo(currentX, currentY, duration = 0.1)

    def setWindowStatus(self, window=None):
        sleep(1)
        global currentTime
        global maxValStr
        global isDoneQueing
        while not isDoneQueing:
            print(f'{currentTime}, {maxValStr}, {self.isDone}')
            if window.isQueing:
                window.setStatusQueue(f'{currentTime}, {maxValStr}')

            arr = [int(i) for i in  currentTime.split(':')]
            arr[1] += 1
            if(arr[1] == 60):
                arr[0] += 1
                arr[1] -= 60
            currentTime = f'{arr[0]}:{'0' if arr[1] < 10 else ''}{arr[1]}'

            sleep(1)

    def findQueue(self, buttonImg, weight, height, inQueueImg, sleepTime, window):
        
        screenshotImg = self.createScreenshot()
        result = cv2.matchTemplate(screenshotImg, buttonImg, cv2.TM_CCOEFF_NORMED)
        _, maxVal, _, maxLoc = cv2.minMaxLoc(result)
        global maxValStr
        maxValStr = str(int(round(maxVal, 2)*100))+'%'
        

        if maxVal >= float(window.config.queueSencitivity):
            self.acceptQueue(maxLoc[0] + weight/2, maxLoc[1] + height/2)
            if(self.isComlete(inQueueImg, sleepTime, window)):
                return True
            return False
        else:
            sleep(sleepTime)
            if self.isDone:
                return True
            return False

    def isComlete(self, inQueueImg, sleepTime, window) -> bool:
        timeRemain = 12
        global maxValStr
        while timeRemain > 0:
            screenshotImg = self.createScreenshot()
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

    def main(self, window = None) -> None:
        buttonImg = cv2.imread('./src/acceptQueue.png', cv2.IMREAD_GRAYSCALE)
        weight = buttonImg.shape[1]
        height = buttonImg.shape[0]

        inQueueImg = cv2.imread('./src/inQueue.png', cv2.IMREAD_GRAYSCALE)

        sleepTime = 1

        global currentTime
        currentTime = '0:01'

        global isDoneQueing
        isDoneQueing = False

        Thread(target=lambda: self.setWindowStatus(window), daemon=True).start()


        while not self.isDone:
            self.isDone = self.findQueue(buttonImg, weight, height, inQueueImg, sleepTime, window)

        isDoneQueing = True
        if window.isQueing:
            window.queueFinder.isDone = True
            window.endQueue()
            if window.config.chatId and window.config.writableToChat:
                requests.get('https://api.telegram.org/bot6736595463:AAHB4szAPZfjbmkTteu73n3aHj1RT1t1dVg/sendMessage?chat_id='+window.config.chatId+'&text=Игра найдена!')

def main(window = None):
    queueFinder = QueueFinder()
    queueFinder.main(window)

if __name__ == '__main__':
    queueFinder = QueueFinder()
    queueFinder.main()