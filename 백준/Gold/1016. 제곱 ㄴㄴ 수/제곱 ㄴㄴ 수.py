import sys
input = sys.stdin.readline

Min, Max = map(int,input().split())
stop = int(Max**(0.5))+1
already = set()
fake = set()

for i in range(2,stop):
    if i not in already:
        index = i**2
        while index<=stop:
            if index not in already:
                already.add(index)
            index+=i**2
        start = Min//(i**2)
        while start*(i**2)<=Max:
            fake.add((i**2)*start)
            start+=1
cnt = 0
for i in range(Min, Max+1):
    if i not in fake:
        cnt+=1
print(cnt)