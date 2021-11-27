import io
import sys

_INPUT = """\
6
##
.#
.#
#.
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S1=input()
  S2=input()
  if S1[0]==S2[1]=='.' or S1[1]==S2[0]=='.':
    print('No')
  else:
    print('Yes')