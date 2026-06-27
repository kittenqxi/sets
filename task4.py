n=int(input())
a=input().split()
b=int(a[0])
max_cnt=0
i=0
while i<len(a):
    num=int(a[i])
    cnt=0
    j=0
    while j<len(a):
        if int(a[j])==num:
            cnt+=1
        j+=1
    if cnt>max_cnt:
        max_cnt=cnt
        b=num
    elif cnt==max_cnt and num<b:
        b=num
    i+=1
print(b)
