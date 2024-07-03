def caesarE(key,pt):
    encrypted= ""
    for i in pt:
        encrypted += chr((ord(i) + key)) 
    return encrypted

def caesarD(key,pt):
    decrypted = ""
    for i in pt:
        decrypted += chr((ord(i) - key))
    return decrypted
   
print(f'Encryption : {caesarE(3,'HELLO')}')
print(f'Decryption : {caesarD(3,'KHOOR')}')


