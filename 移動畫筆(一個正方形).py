import turtle
from turtle import *
#這需要教座標
#(0,0是檔案最中間)
#拿起筆
penup()
#移動筆的位置
goto(0,0)
#筆放下
pendown()
#繪製正方形
for i in range(4):
    forward(50)
    left(90)
done()
