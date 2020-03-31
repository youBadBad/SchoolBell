import time
from playsound import playsound


ONCLASSTIME = [8.00,8.50,9.50,10.40,13.20,14.10,15.00,15.50,16.40,]

class mt():# my time 
    def __init__(self,input:float):
        self.input = input
        self.hour  = int(input)
        self.min   = round((input-self.hour)*100) # 四舍五入

    def plusMin(self,min:int):
        # min > 0
        self.hour += int(min / 60)
        min = min % 60
        temp = self.min+min
        if temp >= 60:
            self.min = temp - 60
            self.hour+= 1
        else:
            self.min = temp
        return self 

    def justis(self,hour,min):
        return self.hour==int(hour) and self.min==int(min)
    
    def toString(self):
        return "{:02d}:{:02d}".format(self.hour,self.min)


def mainLoop():
    a = [[mt(i),mt(i).plusMin(40)] for i in ONCLASSTIME]

    while True:
        time.sleep(5)
        t = time.localtime()
        # print(t)
        
        for i,j in a:
            if i.justis(t.tm_hour,t.tm_min):
                playsound('BUAAonClass.mp3')
                time.sleep(60)
                break
            if j.justis(t.tm_hour,t.tm_min):
                playsound('BUAAoffClass.mp3')
                time.sleep(60)
                break


if __name__ == "__main__":
    mainLoop()
