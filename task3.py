total=int(input())
count=int(input())
st=set(input().split())
c=1
while c<=total:
    if str(c) not in st:
        print(c, end=' ')
    c+=1