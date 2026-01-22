#need more work but this is just visualizer for the chart candle/rollercoaster
#it creates image to share
#still highly under development!!!

import cv2
import numpy as np
import random
import os
from autotrade import *

chart_background_ref = "resources/imgs/chart_background.png"
path = "chart_00000.png"


def create_chart_image():
    return cv2.imread(chart_background_ref, cv2.IMREAD_COLOR)



def chart_numbers(img):
    write_numbers_graph(cv2.putText,img,cv2.FONT_HERSHEY_SIMPLEX)
    pass

def chart_increase_rate(image):
    base = 30
    pass

def chart_draw_progress(image,stock):
    DrawRollerCoster(cv2.line,stock,image)

def chart_save_image(image):
    cv2.imwrite(path, image)



def draw_progress_save(image,stock):

    image = cv2.imread(chart_background_ref, cv2.IMREAD_COLOR)

    
