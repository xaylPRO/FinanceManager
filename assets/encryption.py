
def encrypt(value):
    value = str(value)
    encrypted = ""
    for i in range(len(value)-1, -1, -1):
        encrypted += value[i]
    term = ""
    for j in encrypted:
        term += chr(ord(j) + 2)
    return term

def decrypt(value):
    decrypted = ""
    for i in str(value):
        decrypted += chr(ord(i)-2)

    term = ""
    for j in range(len(decrypted)-1, -1, -1):
        term += decrypted[j]

    return term



