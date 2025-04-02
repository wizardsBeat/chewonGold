import sys
input = sys.stdin.readline

def cal(cf, num): # calculation formula, number
  if num > n:
    if eval(cf.replace(" ", "")) == 0: # replace " " to calculate string
      print(cf)
  
  else:
    # in ASCII code order
    cal(f"{cf} {num}", num + 1)
    cal(f"{cf}+{num}", num + 1)
    cal(f"{cf}-{num}", num + 1)

t = int(input())
for _ in range (t):
  n = int(input())
  cal("1", 2)
  print()