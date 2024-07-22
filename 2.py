n = int(input("Number: "))
sum = 0


for i in range(3, (n - (n%3))+1, 3):
    sum += i

for i in range(5, (n - (n%5))+1, 5):
    sum += i

for i in range(15, (n - (n%15))+1, 15):
    sum -= i



if n%3 == 0 or n%5 == 0:
    sum -= n




print(sum)


