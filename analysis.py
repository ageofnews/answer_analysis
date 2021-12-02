database = []
count = 0
total_len = 0



with open("reviews.txt", "r") as files:
	for line in files:
		database.append(line)
		count += 1  # count = count + 1
		if count % 100000 == 0:   #每100000筆留言印出來 , % = 求餘數
			print(len(database))
			print(line)
			print("----------------------------------")



# 算出這些留言的平均長度!
database_02 =[]

with open("reviews.txt", "r") as action:

	for each_reviews in action:
		database_02.append(each_reviews)
		total_len = total_len + len(each_reviews)
		print(total_len)

print(len(database_02))
print(total_len)
print("平均長度 : ", total_len / len(database_02))
		
