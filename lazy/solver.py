def rev(s):
    return s[::-1]

def encXor(flag):
    key = 7
    encrypted_flag = ''.join(chr(ord(c) ^ key) for c in flag)
    return encrypted_flag

def cipher(s):
    encrypted = ""
    for c in s:
        if c.isalpha():
            if c.isupper():
                encrypted += chr((ord(c) - 65 + 10) % 26 + 65)
            else:
                encrypted += chr((ord(c) - 97 + 10) % 26 + 97)
        else:
            encrypted += c
    return encrypted

def decrypt_cipher(s):
    encrypted = ""
    for c in s:
        if c.isalpha():
            if c.isupper():
                encrypted += chr((ord(c) - 65 - 10) % 26 + 65)
            else:
                encrypted += chr((ord(c) - 97 - 10) % 26 + 97)
        else:
            encrypted += c
    return encrypted

def rot13(s):
    encrypted = ""
    for c in s:
        if c.isalpha():
            if c.isupper():
                encrypted += chr((ord(c) - 65 + 13) % 26 + 65)
            else:
                encrypted += chr((ord(c) - 97 + 13) % 26 + 97)
        else:
            encrypted += c
    return encrypted

def encrypt(s):
    return rev(cipher(rot13(encXor(s))))

def decrypt(s):
    return encXor(rot13(decrypt_cipher(rev(s))))


c = decrypt("wp3laU4lpUz4f67jUq3lUhh4iq3L|")
# c = encrypt("Hello, World!")

print(c)
