import sys

line = sys.stdin.readline().strip()
val = 0
i=0
d = {'a' : 10, 'b' : 11, 'c' : 12, 'd' : 13, 'e' : 14, 'f' : 15}

if (line[0] == '0'):
    if (line[1] == 'x'):
        new_line = list(line[2:])
        new_line.reverse()
        while i < len(new_line):
            if new_line[i].isdigit():
                val += (16**i) * int(new_line[i])
                i+=1
            else:
                val += (16**i) * d[new_line[i]]
                i+=1
    else:
        new_line = list(line[1:])
        new_line.reverse()
        while i < len(new_line):
            val += (8**i) * int(new_line[i])
            i+=1
    print(val)
else:
    print(int(line))