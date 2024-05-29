import turtle
from turtle import * #導入繪圖函式庫

#基本語法
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# done() 
#一定要有這個喔~不然程式會停不下來!

#進階題:(使用迴圈造正方形for)
for i in range(4):
    forward(100)
    left(90)
done()   

#進階題:(使用迴圈造正方形while)
count = 0
while count < 4:
    forward(100)
    left(90) 
    count = count + 1 
done()   

#想想看: 能不能使右邊呢