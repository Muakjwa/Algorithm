stk=[]
while True:
    s=input()
    if s=='.':
        break
    for i in s:
        if i=='(' or i=='[':
            stk.append(i)
        elif i==')':
            if stk==[] or stk[-1]=='[':
                print('no')
                stk=['.']
                break
            else:
                stk.pop()
        elif i==']':
            if stk==[] or stk[-1]=='(':
                print('no')
                stk=['.']
                break
            else:
                stk.pop()
    if stk==[]:
        print('yes')
    elif stk==['.']:
        pass
    else:
        print('no')
    stk=[]