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

# 進階寫法
# good = [d for d in data if 'good' in d]
# print(len(good))


bad = []
for d in data:
	bad.append('bad' in d)
print(bad)
# 進階寫法
# bad = ['bad' in d for d in data]
# print(len(bad))


print(data[0])
wc = {} #word_count #字典使用方式
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
for word in wc:
	if wc[word] >= 1000000:
		print(word, wc[word])
while True:
	word = input('請輸入想查詢字串:')
	if word == 'q':
		break
	if word in wc:
		print(word,'出現次數為', wc[word])
	else:
		print('查無此字串')
print('感謝使用本查詢功能')	


















