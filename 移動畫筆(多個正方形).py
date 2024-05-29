import turtle
from turtle import *

#拿起筆
penup()
#移動筆的位置
goto(-150,150)
#筆放下
pendown()
#繪製正方形
for i in range(4):
    forward(100)
    left(90)

#拿起筆
penup()
#移動筆的位置
goto(-150,-150)
#筆放下
pendown()
#繪製正方形
for i in range(4):
    forward(100)
    left(90)

#拿起筆
penup()
#移動筆的位置
goto(150,150)
#筆放下
pendown()
#繪製正方形
for i in range(4):
    forward(100)
    left(90)

#拿起筆
penup()
#移動筆的位置
goto(150,-150)
#筆放下
pendown()
#繪製正方形
for i in range(4):
    forward(100)
    left(90)
done()