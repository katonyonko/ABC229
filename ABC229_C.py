import io
import sys

_INPUT = """\
6
3 5
3 1
4 2
2 3
4 100
6 2
1 5
3 9
8 7
10 3141
314944731 649
140276783 228
578012421 809
878510647 519
925326537 943
337666726 611
879137070 306
87808915 39
756059990 244
228622672 291
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,W=map(int,input().split())
  cheeze=[list(map(int,input().split())) for _ in range(N)]
  cheeze.sort(key=lambda x: -x[0])
  idx=0
  ans=0
  while W>0 and idx<N:
    a,b=cheeze[idx]
    tmp=min(W,b)
    ans+=tmp*a
    W-=tmp
    idx+=1
  print(ans)