
python에서 입력받을 때, 
```
import sys

A = int(sys.stdin.readline().strip())
```
을 사용해준다. 시간 절약


python 에서 재귀함수를 돌릴 때,
```
import sys

sys.setrecursionlimit(1000000)
```
을 적어준다. python에는 재귀에 제한이 걸려있어 
해당 코드를 적어주지 않으면 runtime error(recursion limit)이 발생한다.