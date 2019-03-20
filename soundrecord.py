data = []
count = 0
with open('reviews.txt', 'r') as msg:
	for m in msg:
		data.append(m)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
	
print('留言的平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '比留言長度小於100')
print(new[0])
print(new[1])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])
print(good[1])