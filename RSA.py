from RSAresources import *

class RSA:
    
    def __init__(self, e=65537, P=generatePrime(), Q = generatePrime()):
        
        self.e = e
        self.P = P
        self.Q = Q
        
        
        while not coprime(e,P) and not coprime(e,Q):
            self.P = generatePrime()
            self.Q = generatePrime()
            
        self.N = P * Q
        self.public = [self.e, self.N]
        self.phi = (Q-1)*(P-1)
        self.d = mod_inverse(self.e, self.phi)
        self.private = [self.d, self.N]
    
        
    def encrypt(self,msg):
        try:
            return pow(msg,self.e, self.N)
        except TypeError:                   #if it's a type error, probably tried to encrypt text
            return self.encryptText(msg)
        except:
            print("THERE WAS AN ERROR!")
    
    def encryptText(self,msg):
        msg = devIntoBlocks(msg)
        return [self.encrypt(block) for block in msg]
        
    def decrypt(self, msg, d= 0, N= 0):
        if not d and not N:
            d = self.d
            N = self.N
        try:
            return pow(msg, self.d, self.N)
        
        except TypeError:
            return self.decryptText(msg)
        
        except:
            print("THERE WAS AN ERROR!")
            
    def decryptText(self, msg):
        msg = [self.decrypt(block) for block in msg]

    def signature(self, msg, d=0, N=0):
        if not d or not N:
            d = self.d
            N = self.N
            
        import hashlib
        
        try:
            return str(pow(int(hashlib.sha256(msg.encode()).hexdigest(), 16), d, N))
            
        except: 
            return pow(int(hashlib.sha256(msg.encode()).hexdigest(), 16), d, N)
        
        
    def verify(self, msg, sig, N=0, e=65537):
        if not e and not N:
            e = self.e
            N = self.N
            
        import hashlib
            
        return pow(int(sig),e,N) == int(hashlib.sha256(msg.encode()).hexdigest(), 16)
    
    def hash(self,msg):
        import hashlib
        return int(hashlib.sha256(msg.encode()).hexdigest(), 16)
