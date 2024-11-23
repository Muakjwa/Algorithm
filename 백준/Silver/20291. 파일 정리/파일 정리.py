N = int(input())

ext_dict = dict()

for _ in range(N):
    file_ext = input().split('.')[1]
    if file_ext in ext_dict.keys():
        ext_dict[file_ext] += 1
    else:
        ext_dict[file_ext] = 1

for ext in sorted(list(ext_dict.keys())):
    print(ext, ext_dict[ext])