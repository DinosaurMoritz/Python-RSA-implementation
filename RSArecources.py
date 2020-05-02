from Crypto.Util import number

def generatePrime(leng=1024):
	return number.getPrime(leng)

def mod_inverse(x,y):

	def eea(a,b):
		if b==0:return (1,0)
		(q,r) = (a//b,a%b)
		(s,t) = eea(b,r)
		return (t, s-(q*t) )

	inv = eea(x,y)[0]
	if inv < 1: inv += y
	return inv
	

from math import gcd as bltin_gcd

def coprime(a, b):
    return bltin_gcd(a, b) == 1
