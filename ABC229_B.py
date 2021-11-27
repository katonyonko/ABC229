import io
import sys

_INPUT = """\
6
229 390
123456789 9876543210
9 81
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A,B=input().split()
  m=min(len(A),len(B))
  ans='Easy'
  for i in range(m):
    if int(A[~i])+int(B[~i])>=10:
      ans='Hard'
  print(ans)