import sys

N = int(sys.stdin.readline().strip())

for _ in range(N):
    students = list(map(int, sys.stdin.readline().strip().split()))
    sorted_students = []
    total_step = 0
    for i in range(1, len(students)):
        cnt = 0
        if i == 1:
            sorted_students.append(students[1])
        else:
            for j in range(len(sorted_students)):
                if sorted_students[j] > students[i]:
                    sorted_students.insert(j, students[i])
                    total_step += (len(sorted_students) - 1 - j)
                    break
                elif j+1 == len(sorted_students):
                    sorted_students.append(students[i])
                    break
                else:
                    cnt += 1

    print(students[0], total_step)