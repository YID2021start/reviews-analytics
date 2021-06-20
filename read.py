data =  []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了,總共有',len(data),'筆資料')	

sum_len = 0
for d in data:
	sum_len += len(d)
print('每則留言平均字數為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有',len(new),'筆留言小於100')
		

good = []
for d in data:
	if 'good' in d:
		good.append(d)

#進階寫法
good = [d for d in data if 'good' in d]
print(len(good))


bad = []
for d in data:
	bad.append('bad' in d)
print(bad)	

#進階寫法
bad = ['bad' in d for d in data]
print(len(bad))
