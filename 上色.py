import turtle
from turtle import *

#選擇填滿
begin_fill()
#選擇顏色
#顏色可以用RGB16進位格式去寫(例如:#123456)
color('red')
#繪製圖案
for i in range(4):
    forward(100)
    left(90)
#結束填滿
end_fill()
#結束繪畫
done()