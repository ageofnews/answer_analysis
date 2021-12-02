
good = []
bad = []

with open("reviews.txt", "r") as action:



	good = [data for data in action]
	print(len(good))
# with open("reviews.txt", "r") as action:
	bad = [data2 for data2 in action if "bad" in data2]
	print(len(bad))