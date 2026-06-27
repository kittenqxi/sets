n=int(input())
pfr=input().split()
m=int(input())
vfr=input().split()
vset=set(vfr)
count=0
ii=0
while ii<len(pfr):
    i=pfr[ii]
    if i in vset:
        count+=1
    ii+=1
print(count)