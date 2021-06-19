data = []
x = 0
g = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		x = x + len(data[g])
		g += 1
	print('每則留言平均數是',x/len(data))