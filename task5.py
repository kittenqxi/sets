py=set(input().split())
sql=set(input().split())
lin=set(input().split())
alls=list(py|sql|lin)
onlyp=0
twoc=0
thc=0
lo=len(alls)
i=0
while i<len(alls):
    student=alls[i]
    count=0
    if student in py:
        count+=1
    if student in sql:
        count+=1
    if student in lin:
        count+=1
    if count==1 and student in py:
        onlyp+=1
    elif count==2:
        twoc+=1
    elif count==3:
        thc+=1
    i+=1
print(onlyp)
print(twoc)
print(thc)
print(lo)