import random
data = []
with open('reviews.txt', 'r')as value:
	for line in value:
		data.append(line)
r = random.randint(0,len(data)-1)
print(data[r])