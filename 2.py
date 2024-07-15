S = input("S: ")

for i in S[ : 100]:
    if i.isalnum():

        if S.count(i) > 1:
            print(i)
            break

else:
    print(-1)
