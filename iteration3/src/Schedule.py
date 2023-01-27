
class Schedule:
    def __init__(self,day,startingTime):
        self._day = day
        self._startingTime = startingTime

    def checkCollision(self,schedule):
        if self._day == schedule.getDay() and self._startingTime == schedule.getStartingTime():
            return True
        return False
    
    def getDay(self):
        return self._day
    
    def getStartingTime(self):
        return self._startingTime
    
    def setDay(self,day):
        self._day = day

    def setStartingTime(self,startingTime):
        self._startingTime = startingTime