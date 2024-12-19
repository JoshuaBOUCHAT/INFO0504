import FBijection8bitsCA as FBI8
import Message

def mybij(octet,number):
    return octet ^ number

class FBijParDecallage(FBI8.FBijection8bitsCA):
    def __init__(self,number):
        self.bijection = mybij
        self.number = number
    
    def __repr__(self):
        return f'{self.number}'
    def __call__(self, octet):
        return self.bijection(octet,self.number)
    def valInv(self, octetC):
        return self.bijection(octetC,self.number)
    

if __name__ == "__main__":
    fbi = FBijParDecallage(50)
    fbi.afficheGraphiquesDeDiffusionConfusion()

