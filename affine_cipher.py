alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def encrypt(plaintext,alpha,beta):
    if gcd(alpha,len(alphabet)) != 1:
        return
    ciphertext = ""
    for char in plaintext:
        index = alphabet.index(char)
        index = (alpha*index + beta) % len(alphabet)
        ciphertext += alphabet[index]
    return ciphertext

def decrypt(ciphertext,alpha,beta):
    plaintext = ""
    for char in ciphertext:
        index = alphabet.index(char)
        index = ( inverseOf( alpha, len(alphabet) ) * ( index - beta) ) % len(alphabet)
        plaintext += alphabet[index]
    return plaintext

def gcd(i,j):
    rem = i % j
    if rem == 0 :
        return j
    return gcd(j,rem)

def inverseOf(i,mod):
     i = i % mod
     inverse = 2
     while (i * inverse) % mod != 1:
         inverse += 1
     return inverse % mod 
    
print(encrypt("hello",3,1), decrypt("wniir",3,1))
