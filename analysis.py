database = []
count = 0


with open("reviews.txt", "r") as files:
	for line in files:
		database.append(line)
		count += 1  # count = count + 1
		if count % 100000 == 0:   #每100000筆留言印出來
			print(len(database))
			print(line)
			print("----------------------------------")