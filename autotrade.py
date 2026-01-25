#the core file of autotrade

class Stock:
    def __init__(self, name):
        self.candle = []
        self.stock_name = name
    
    def add_candle(self,time,value):
        self.candle.append({"time" : time, "value" : value})



def get_rate(origin,current):
    change_rate = 0
    if current != 0 and origin != 0:
        change_rate = ((current-origin) / origin) * origin
    return change_rate


def GetStock(): #fprintf open stock asserted file
    FILE_point = open("data/stock.stk","r")
    foo = ""
    temp = " "
    while temp != "":
        temp = FILE_point.read(1)
        if temp == "\n" or temp == " " or temp == "":
            pass
        else:
            foo += temp
    return foo
