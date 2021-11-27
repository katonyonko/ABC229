import io
import sys

_INPUT = """\
6
XX...X.X.X.
2
XXXX
200000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  N=len(S)
  K=int(input())
  ans=0
  idx=0
  while idx<N and (K>0 or S[idx]=='X'):
    ans+=1
    if S[idx]=='.':
      K-=1
    idx+=1
  tmp=ans
  for i in range(1,N):
    tmp-=1
    if S[i-1]=='.':
      K+=1
    while idx<N and (K>0 or S[idx]=='X'):
      tmp+=1
      if S[idx]=='.':
        K-=1
      idx+=1
    ans=max(ans,tmp)
  print(ans)