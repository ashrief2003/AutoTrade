#just mere api that abstracts opencv functions and make them simpler, cleaner


import cv2
import numpy as np
import random
import os
from autotrade import *

chart_background_ref = "resources/imgs/chart_background.png"
path = "chart_00000.png"


#keep
def create_chart_image(): #make the image
    return cv2.imread(chart_background_ref, cv2.IMREAD_COLOR)

def write_text(img ,print_text ,vector , color = (255,255,255),fontsize = 1):#draw text
    default_font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,print_text,vector,default_font,fontsize,color,1)

def DrawLine(img,v1,v2 ,color = (255,255,255)): #drawline
    cv2.line(img,v1,v2, color, 2)
    #DrawRollerCoster(cv2.line,stock,image)


def chart_save_image(image): #save it as image
    cv2.imwrite(path, image)


#check
def candle_rate():
    write_rate(cv2.putText,img,cv2.FONT_HERSHEY_SIMPLEX)
    
