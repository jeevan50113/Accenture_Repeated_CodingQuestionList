def Decrypt(str):
    if str is None:
        return None
    
    decrypted_str = ''.join(chr(219 - ord(c)) for c in str)
    
    return decrypted_str


print(Decrypt("hii"))