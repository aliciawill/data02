buy = []
wish = list()

for _ in range(0, 5): #[0,1,2,3,4]
    buy.append(input('사고 싶은 것>>'))


print(buy)

# c방식
for i in  range(0,5):
    print(buy[i])

#for-each방식
for e in buy:
    print(e)

