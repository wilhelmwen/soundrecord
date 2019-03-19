data = []
count = 0
with open('reviews.txt', 'r') as msg:
	for m in msg:
		data.append(m)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print(len(data))

print(data[0])
print('-----------------')
print(data[1])