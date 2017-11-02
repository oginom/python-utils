def gcf(n, m):
	if n > m:
		l = n
		n = m
		m = l
	while n != 0:
		l = n
		n = m % n
		m = l
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
				ret.append(d)
				n //= d
				break
			else:
				#print('probably,')
				ret.append(n)
				return ret
	return hulistic(n, ret)

def hulistic(n, known=None):
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
		n = int(input('input number to prime factorize : '))
		if not n > 0:
			break
		ret = rho(n)
		print(ret)
	print('end.')
