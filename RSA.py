
from RSAresources import *

class RSA:
	
	def __init__(self,e=65537,P=generatePrime(),Q = generatePrime()):
		
		self.e = e
		self.P = P
		self.Q = Q
		
		
		while not coprime(e,P) and not coprime(e,Q):
			self.P = generatePrime()
			self.Q = generatePrime()
			
		self.N = P * Q
		self.public = [self.e,self.N]
		self.phi = (Q-1)*(P-1)
		self.d = mod_inverse(self.e,self.phi)
		self.private = [self.d,self.N]
		
	def encrypt(self,msg,t=False):
		if t:
			return self.encryptText(msg)
		return pow(msg,self.e, self.N)
	
	def decrypt(self, msg,d= 0, N= 0):
		if not d and not N:
			d = self.d
			N = self.N
		return pow(msg,d,N)
		

	def encryptText(self ,msg):	
		return "-".join(list(map(lambda x :"".join(list(map(lambda y: str(self.encrypt(ord(y)))+"/",x))),list(map(lambda x: list(x),str(msg).split())))))
		
	def decryptText(self,msg,d=0,N=0):
		if not d and not N:
			d = self.d
			N = self.N
		
		fun = lambda y: 0 if y == '' else int(y)
		
		return " ".join(list(map(lambda x: "".join(x),list(map(lambda x: list(map(lambda y: chr(y),x)),list(map(lambda x: x[:-1],list(map(lambda x: list(map(lambda y: self.decrypt(fun(y),d,N),x)),list(map(lambda x: list(map(lambda y: y.replace("/",""),x)), list(map(lambda x: x.split("/"),msg.split("-"))))))))))))))
		
		
		
