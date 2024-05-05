first = input()
second = input()
explode = []
string = []
for i in second:
    explode.append(i)
for i in first:
    string.append(i)
    if len(string)>=len(explode):
        if string[len(string)-len(explode):len(string)]==explode:
            for _ in range(len(explode)):
                string.pop()
if(len(string)==0):
    print('FRULA')
else:
    print(''.join(string))