t=int(input())
for i in range(0,t):
    s=str(input())

    even_string=''
    odd_string=''

    for j in range(0,len(s)):
        if j%2==0:
            even_string+=(s[j])
        else :
             odd_string+=s[j]
    print(even_string,odd_string)

