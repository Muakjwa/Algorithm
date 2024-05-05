import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
market = {}
combi = {}
num = ['0','1','2','3','4','5','6','7','8','9']

for i in range(N):
    it, price = input().strip().split()
    market[it] = int(price)

for i in range(M):
    r, j = input().strip().split('=')
    jaryo = list(j.split('+'))
    jaryo_list = {}
    for jar in jaryo:
        idx = 0
        number = ''
        while True:
            if jar[idx] in num:
                number+=jar[idx]
                idx+=1
            else:
                break
        if jar[idx:] in jaryo_list:
            jaryo_list[jar[idx:]]+=int(number)
        else:
            jaryo_list[jar[idx:]] = int(number)
    if r in combi:
        combi[r].append(jaryo_list)
    else:
        combi[r] = [jaryo_list]


def make(something):
    for i in range(len(combi[something])):
        cost = 0
        G = True
        for jaryo in list(combi[something][i].keys()):
            if jaryo not in market:
                G = False
                break
            else:
                cost += market[jaryo] * combi[something][i][jaryo]
        if G ==True:
            if something not in market:
                if cost>1e9:
                    market[something] = int(1e9+1)
                else:
                    market[something] = cost
            else:
                if min(market[something], cost)>1e9:
                    market[something] = int(1e9+1)
                else:
                    market[something] = min(market[something], cost)

for i in range(51):
    for something in list(combi.keys()):
        make(something)
if 'LOVE' in market:
    print(market['LOVE'])
else:
    print(-1)