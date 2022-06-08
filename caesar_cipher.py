alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def encrypt(plaintext,key):
    ciphertext = ""
    for char in plaintext:
        index = alphabet.index(char)
        index = (index + key) % len(alphabet)
        ciphertext += alphabet[index]
    return ciphertext

def decrypt(ciphertext,key):
    plaintext = ""
    for char in ciphertext:
        index = alphabet.index(char)
        index = (index - key) % len(alphabet)
        plaintext += alphabet[index]
    return plaintext