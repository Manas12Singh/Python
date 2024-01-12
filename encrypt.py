def caesar_encrypt(plain_text: str, key: int) -> str:
    cipher_text = ""
    for i in plain_text:
        if i.isalpha():
            if i.isupper():
                cipher_text += chr((ord(i) + key - 65) % 26 + 65)
            else:
                cipher_text += chr((ord(i) + key - 97) % 26 + 97)
        else:
            cipher_text += i
    return cipher_text


def caesar_decrypt(cipher_text: str, key: int) -> str:
    plain_text = ""
    for i in cipher_text:
        if i.isalpha():
            if i.isupper():
                plain_text += chr((ord(i) - key - 39) % 26 + 65)
            else:
                plain_text += chr((ord(i) - key - 71) % 26 + 97)
        else:
            plain_text += i
    return plain_text


def vigenere_encrypt(plain_text: str, key: str) -> str:
    cipher_text = ""
    key_len = len(key)
    for j in range(len(plain_text)):
        if plain_text[j].isupper():
        cipher_text += plain_text[j] + key[j % key_len]
    return cipher_text


p = "Hello, World!"
k = "Kim"
e = vigenere_encrypt(p, k)

print(p)
print(e)
# print(d)

'''

'''