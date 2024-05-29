import random
import turtle
from turtle import * #導入繪圖函式庫

for i in range(5):
    penup()
    goto(random.randint(-200,200),random.randint(-200,200))
    pendown()
    for i in range(4):
        forward(50)
        left(90)
done()