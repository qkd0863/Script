import time


class StopWatch:
    def __init__(self):
        __startTime = time.time()
        __endTime = 0

    def getStartTime(self):
        return self.__startTime

    def getEndTime(self):
        return self.__endTime

    def start(self):
        self.__startTime = time.time()

    def stop(self):
        self.__endTime = time.time()

    def getElapsedTime(self):
        return int((self.__endTime - self.__startTime) * 1000)


s = StopWatch()
result = 0
s.start()
for i in range(1, 1000001):
    result += i
s.stop()
print("경과시간:", s.getElapsedTime())



