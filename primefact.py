#!/usr/bin/env python3

def gcf(n, m):
  if n > m:
    n, m = m, n
  while n != 0:
    n, m = m % n, n
  return m

def rho(n):
  ret = []
  while n > 1000:
    x = 1
    y = 2
    while True:
      d = gcf(abs(x - y), n)
      if d == 1:
        x = (x * x + 1) % n
        y = (y * y + 1) % n
        y = (y * y + 1) % n
      elif d < n:
        ret.extend(rho(d))
        n //= d
        break
      else:
        #print('probably,')
        ret.append(n)
        return ret
  return trialdiv(n, ret)

def trialdiv(n, known=None):
  ret = []
  if known:
    ret = known
  p = 2
  while n > 1:
    if n % p == 0:
      ret.append(p)
      n //= p
    else:
      p += 1
  return ret

if __name__ == '__main__':
  while True:
    try:
      n = int(input('input number to prime factorize : '))
    except:
      break
    if not n > 0:
      break
    ret = rho(n)
    print(ret)
  print('end.')
