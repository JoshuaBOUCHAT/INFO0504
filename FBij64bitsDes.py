tPI = [58, 50, 42, 34, 26, 18, 10, 2,60, 52, 44, 36, 28, 20, 12, 4,62, 54, 46, 38, 30, 22, 14, 6,64, 56, 48, 40, 32, 24, 16, 8,57, 49, 41, 33, 25, 17, 9, 1,59, 51, 43, 35, 27, 19, 11, 3,61, 53, 45, 37, 29, 21, 13, 5,63, 55, 47, 39, 31, 23, 15, 7]
tPIm1=[40, 8, 48, 16, 56, 24, 64, 32,39, 7, 47, 15, 55, 23, 63, 31,38, 6, 46, 14, 54, 22, 62, 30,37, 5, 45, 13, 53, 21, 61, 29,36, 4, 44, 12, 52, 20, 60, 28,35, 3, 43, 11, 51, 19, 59, 27,34, 2, 42, 10, 50, 18, 58, 26,33, 1, 41, 9, 49, 17, 57, 25]
SBOX = [
# Box-1
[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],
[[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],
[[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]],
[[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]],
[[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]],
[[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]],
[[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]],
[[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]]

F_PBox =   [16, 7, 20, 21, 29, 12, 28, 17,1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9,19, 13, 30, 6, 22, 11, 4, 25 ]
key_PBox = [14,17, 11,24, 1,5,3,28, 15, 6,21, 10,23,19, 12, 4,26,8, 16, 7, 27,20,13,2,41,52, 31,37,47, 55,30,40, 51,45,33, 48,44,49, 39,56,34,53, 46,42, 50,36,29, 32]

tPC1=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
tPC2=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
tv=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

tEBox = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
tP = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]



class FBij64BitsDES(object):
    def __init__(self, cle, verbose=False):
        self.cle = cle
        self.verbose = verbose
        self.sousCles = self.liste16Cles(intToListBits(cle, 64))

    def __repr__(self):
        return f"FBij64BitsDES(cle={self.cle:016x}, verbose={self.verbose})"

    def __call__(self, mot64bits):
        """
        >>> hex(FBij64BitsDES(0x0e329232ea6d0d73)(0x8787878787878787))
        '0x0'
        >>> hex(FBij64BitsDES(0x123556789ABDDEF0)(0x0123456789ABCDEF))
        '0x85e813540f0ab405'
        """
        lbits = intToListBits(mot64bits, 64)
        return self.chiffre(lbits)

    def valInv(self, mot64bitsChiffre):
        """
        >>> hex(FBij64BitsDES(0x0e329232ea6d0d73).valInv(0x0000000000000000))
        '0x8787878787878787'
        >>> hex(FBij64BitsDES(0x123556789ABDDEF0).valInv(0x85e813540f0ab405))
        '0x0123456789abcdef'
        """
        lbits = intToListBits(mot64bitsChiffre, 64)
        return self.dechiffre(lbits)

    def liste16Cles(self, lbKey):
        """
        Renvoie un tableau de 17 éléments mais seules les clés 1 à 16 sont initialisées
        """
        # Permutation initiale de la clé
        lbKey56 = lbImage(lbKey, tPC1)

        # Division de la clé en deux moitiés
        C0 = lbKey56[:28]
        D0 = lbKey56[28:]

        # Tableau pour stocker les sous-clés
        sousCles = [None] * 17

        # Génération des sous-clés
        for i in range(1, 17):
            # Rotation des moitiés de la clé
            C0 = C0[tv[i-1]:] + C0[:tv[i-1]]
            D0 = D0[tv[i-1]:] + D0[:tv[i-1]]

            # Combinaison des moitiés de la clé
            C0D0 = C0 + D0

            # Permutation finale de la clé
            sousCles[i] = lbImage(C0D0, tPC2)

            if self.verbose:
                print(f"Sous-clé {i}: {txtH(sousCles[i])}")

        return sousCles

    def chiffre(self, lbits):
        # Permutation initiale (IP)
        lb64 = lbImage(lbits, tPI)

        # Division en deux moitiés
        L0 = lb64[:32]
        R0 = lb64[32:]

        # Application des 16 rounds
        for i in range(1, 17):
            # Application de la fonction F
            lb32_f = functionF(R0, self.sousCles[i])

            # XOR avec la moitié gauche
            R1 = [L0[j] ^ lb32_f[j] for j in range(32)]

            # Mise à jour des moitiés
            L0, R0 = R0, R1

        # Combinaison des moitiés
        L1R1 = R0 + L0

        # Permutation finale (IP^-1)
        lb64_final = lbImage(L1R1, tPIm1)

        return listBitsToInt(lb64_final)

    def dechiffre(self, lbits):
        # Permutation initiale (IP)
        lb64 = lbImage(lbits, tPI)

        # Division en deux moitiés
        L0 = lb64[:32]
        R0 = lb64[32:]

        # Application des 16 rounds en ordre inverse
        for i in range(16, 0, -1):
            # Application de la fonction F
            lb32_f = functionF(R0, self.sousCles[i])

            # XOR avec la moitié gauche
            R1 = [L0[j] ^ lb32_f[j] for j in range(32)]

            # Mise à jour des moitiés
            L0, R0 = R0, R1

        # Combinaison des moitiés
        L1R1 = R0 + L0

        # Permutation finale (IP^-1)
        lb64_final = lbImage(L1R1, tPIm1)

        return listBitsToInt(lb64_final)

# Fonctions auxiliaires
def lbImage(lbits, tPermutation):
    """
    Renvoie l'image d'une liste de bits par une permutation
    """
    return [lbits[i-1] for i in tPermutation]

def intToListBits(val, taille):
    """
    Convertit un entier en une liste de bits de longueur spécifiée
    """
    k = val
    lbits = []
    while k > 0:
        lbits = [k & 0b0001] + lbits
        k = k >> 1
    assert taille - len(lbits) >= 0, "Nombre trop grand !!"
    return (taille - len(lbits)) * [0] + lbits

def listBitsToInt(lbits):
    """
    Convertit une liste de bits en un entier
    """
    res = 0
    for bit in lbits:
        res = (res << 1) | bit
    return res

def txtH(lbits):
    """Une string représentant le nombre en hexa avec tous ses chiffres
    >>> txtH([0,0,0,0,1,0,1,1,0,0,1,1,1])
    '0167'
    >>> txtH([0,0,0,0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1])
    '0167'
    """
    s = ""
    val = 0
    l = len(lbits)
    for k, c in enumerate(lbits):
        val = val * 2 + int(c)
        if ((l - 1 - k) % 4 == 0):
            s += f"{val:0x}"
            val = 0
    return s

def lbSImage(lb6bits, sBoxNum):
    """ Image d'un mot de 6bits par la Sbox numéro sBoxNum
    >>> lbSImage([0,1,1,0,0,0], 0)
    [0, 1, 0, 1]
    >>> lbSImage([1,0,0,1,1,1], 7)
    [0, 1, 1, 1]
    """
    row = int(f"{lb6bits[0]}{lb6bits[5]}", 2)
    col = int(f"{lb6bits[1]}{lb6bits[2]}{lb6bits[3]}{lb6bits[4]}", 2)
    sbox_value = SBOX[sBoxNum][row][col]
    return intToListBits(sbox_value, 4)

def functionF(lb32, lbkey48bits):
    """ Image d'un mot de 32bits par la fonction f avec une clé de 48bits
    >>> txtH(functionF(intToListBits(0xff0000ff,32), intToListBits(0x36146478e1e1,48)))
    'a393e878'
    """
    # Expansion de la moitié droite
    lb48 = lbImage(lb32, tEBox)

    # XOR avec la clé
    lb48_xor = [lb48[i] ^ lbkey48bits[i] for i in range(48)]

    # Substitution (S-Boxes)
    lb32_sbox = []
    for i in range(8):
        lb6bits = lb48_xor[i*6:(i+1)*6]
        lb32_sbox.extend(lbSImage(lb6bits, i))

    # Permutation (P)
    lb32_p = lbImage(lb32_sbox, tP)

    return lb32_p

# Exemple d'utilisation
if __name__ == "__main__":
    import doctest
    doctest.testmod()

    f = FBij64BitsDES(0x123556789ABDDEF0)
    print(hex(f(0x0123456789ABCDEF)))  # Output: '0x85e813540f0ab405'
    print(hex(f.valInv(0x85e813540f0ab405)))  # Output: '0x0123456789abcdef'