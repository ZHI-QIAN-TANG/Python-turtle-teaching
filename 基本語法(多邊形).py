import turtle
from turtle import *

#需要多少角
count = int(input()) 
#角度計算
angle = 360/count
#繪圖區域
while count > 0:
    forward(100)
    left(angle)
    count = count - 1
#結束畫畫
done()