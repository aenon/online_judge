# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
e = math.e

def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

def reduce_denom(nom, denom):
  return denom / gcd(nom, denom)

def is_terminating(denom):
  while denom % 2 == 0:
    denom /= 2
  while denom % 5 == 0:
    denom /= 5
  return denom == 1

def get_k(N):
  return int(round(N/e))

q = int(raw_input().strip())
for i in xrange(q):
  n = int(raw_input().strip())
  sumn = 0
  for j in range(5, n + 1):
    k = get_k(j)
    if is_terminating(reduce_denom(j, k)):
      sumn -= j
    else:
      sumn += j
  print(sumn)