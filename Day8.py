t=int(input())
phoneBook=dict()
for i in range(0,t):
    name,number= input().split(" ")
    phoneBook[name]=number

for j in range(0,t):
    name=str(input())

    if name in phoneBook:
        print("{}={}".format(name,phoneBook[name]))
    else:
        print('Not found')
