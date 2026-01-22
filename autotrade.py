#the core file of autotrade




color = (255,255,255) #fixed on white color

class Stock:
    def __init__(self, time, stock_value):
        self.candle = {"time" : time, "stock_value" : stock_value}
        self.stock_name = "stock_name"

def get_rate(origin,current):
    change_rate = ((current-origin) / origin) * origin
    return change_rate


def GetStock():
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


def DrawRollerCoster(drawLineFun,stock,output): #rollercoaster style
    #drawLineFun = cv2.line(), output = image
    #color = (255,255,255) #fixed on white color
    i = 0 
    #base Initialization
    base = 678 - 70
    last_x = (1) * 45
    last_y = base - (stock[0] * 1)
    while i != len(stock):
        x = (i + 1) * 45
        y = base - (stock[i] * 2)
        drawLineFun(output, (last_x, last_y), (x, y), color, 2)
        last_x = x
        last_y = y
        i += 1

def write_numbers_graph(draw_text_fun,output,fontstyle):
    limit = 5
    for i in range(limit):
        draw_text_fun(output,f"{i * 10}",(25,600 - (70 * (i + 1))), 1,fontstyle,color,15)