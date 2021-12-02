#range 範圍
#清單產生器 搭配for loop可以重複執行多次!

range(5)  #[0.1.2.3.4] = range[0,5] 含頭不含尾
for data in range(5):
	print(data)   #可以執行5次!


#隨機產生隨機數
import random
time = input("請輸入隨機次數:")
time = int(time)
for x in range(time):
	print("這是第",x+1,"的隨機數")
	print(random.randint(1,100))


# range[x, y, z]  x開始值(包含)  y結尾值(不包含)    z遞增值

range(2,10,2)
for xxx in range(2, 10, 2):
	print(xxx)