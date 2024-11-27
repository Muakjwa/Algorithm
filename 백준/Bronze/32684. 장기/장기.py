import sys

cho = list(map(int, sys.stdin.readline().strip().split()))
han = list(map(int, sys.stdin.readline().strip().split()))

def cal_score(cho):
    score = cho[0] * 13 + cho[1] * 7 + cho[2] * 5 + cho[3] * 3 + cho[4] * 3 + cho[5] * 2
    return score

cho_score = cal_score(cho)
han_score = cal_score(han) + 1.5

if cho_score>han_score:
    print("cocjr0208")
else:
    print("ekwoo")