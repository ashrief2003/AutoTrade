#script I used to test if functions works or not

from imaging import *
from autotrade import *


stock = [0]

for i in range(20):
    x = random.randint(0, 300)
    print(x)
    stock.append(x)

img = create_chart_image()
chart_numbers(img)
chart_draw_progress(img,stock)
chart_save_image(img)