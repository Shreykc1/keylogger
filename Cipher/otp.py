def otpE(key,pt):
    ptNum = []
    keyNum = []
    sum = []
    
    pt = pt.lower()
    key = key.lower()
    for i in pt:
         ptVal = abs((ord(i) - 97))
         ptNum.append(ptVal)
    for i in key:
         keyVal = abs((ord(i) - 97))
         keyNum.append(keyVal)
    
    for i in range(len(ptNum)):
        sum.append((ptNum[i] + keyNum[i]) % 26)
    
    otp = ''
    for i in sum:
         otp += chr(i + 97)
    return otp


      
    
    



print(otpE("MONEY","HELLO"))