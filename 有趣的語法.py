import turtle
from turtle import *

shape('turtle') #箭頭換成烏龜

#前往定位
goto(10,5)

#設置x座標
setx(10)

#設置y座標
sety(10)

#設置朝向
setheading(90)

#畫圓(半徑,角度)
circle(10,360)

#返回原點
home()

#當前位置
print(position())

#目標方向
print(towards(-10,-10))

#當前朝向
print(heading())

#設定畫筆資訊
print(pensize(70))

#設定畫筆顏色
print(pencolor('red'))

#取得當前畫筆資訊
print(pen())

done()