#script I used to test if functions works or not

from imaging import *
from autotrade import *
from cv2 import *


#-----------pre defined values-------------#

#colors

red = (0, 0, 255) #green

green = (0, 255, 0)#red

#different values



change_rate = []


#-------------------------------------------#





#--------------stocks functions-------------#

def add_profile(vector,value,stock_value):
    return {"vector" : vector, "value" : value, "stock_value" : stock_value}

def draw_vertical_numbers():
    pass

def draw_roller_coster(img,stock): #rollercoaster style
    change_rate = []
    #drawLineFun = cv2.line(), output = image
    #color = (255,255,255) #fixed on white color
    i = 0 
    #base Initialization
    base = 678 - 70
    last_x = (1) * 45
    last_y = base - (stock[0] * 1)
    last_stock = 0
    while i != len(stock):
        x = int((i + 1) * 50 + 45)
        y = int(base - (stock[i] * 2))
        DrawLine(img,(last_x,last_y),(x,y))

        #DrawLine(img,(last_x, last_y), (x, y))
        last_x = x
        last_y = y

        new_rate = get_rate(last_stock,stock[i])
        change_rate.append(add_profile((x,y),new_rate,stock[i]))

        last_stock = stock[i]
        i += 1
    
    for i in range(len(change_rate)):
        vector = change_rate[i]["vector"]
        stk = change_rate[i]["value"]
        stk_chg = change_rate[i]["stock_value"]
        print_rate(img,vector,stk,stk_chg)



def print_rate(img,vector,value,stock_value):
    color = (0,0,0)
    if value >= 0:
        color = green
    elif value < 0:
        color = red

    write_text(img ,f"%{value:.3f} ({stock_value})",vector,color,0.4)


def run_test():

    stock = []

    for i in range(44):
        x = random.randint(45, 100)
        print(x)
        stock.append(x)

    img = create_chart_image()

    draw_roller_coster(img,stock)

    chart_save_image(img)

    

#-------------------------------------------#


x = Stock("google")
x.add_candle("tome",100)
x.add_candle("tome",1213)
print(x.candle)




# chart_numbers(img)
# chart_draw_progress(img,stock)
# chart_increase_rate(img,9,5)
# chart_save_image(img)