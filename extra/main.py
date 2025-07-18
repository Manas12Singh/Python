dict1 = {chr(65 + i): i for i in range(26)}
dict1.update({chr(97 + i): i for i in range(26)})

dict2 = {i: chr(65 + i) for i in range(26)}


def caesar_encrypt(text: str, shift: int) -> str:
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            new_char = chr((dict1[char] + shift) % 26 + base)
            encrypted += new_char
        else:
            encrypted += char
    return encrypted


def caesar_decrypt(cipher: str, shift: int) -> str:
    return caesar_encrypt(cipher, -shift)


def vigenere_encrypt(plain_text: str, key: str) -> str:
    key_len = len(key)
    if key_len == 0:
        return plain_text
    cipher_text = ""
    i = 0
    for j in plain_text:
        if j.isalpha():
            if j.isupper():
                cipher_text += chr((dict1[j] + dict1[key[i % key_len]]) % 26 + 65)
            else:
                cipher_text += chr((dict1[j] + dict1[key[i % key_len]]) % 26 + 97)
            i += 1
        else:
            cipher_text += j
    return cipher_text


def vigenere_decrypt(cipher_text: str, key: str) -> str:
    key_len = len(key)
    if key_len == 0:
        return cipher_text
    plain_text = ""
    i = 0
    for j in cipher_text:
        if j.isalpha():
            if j.isupper():
                plain_text += chr((dict1[j] - dict1[key[i % key_len]]) % 26 + 65)
            else:
                plain_text += chr((dict1[j] - dict1[key[i % key_len]]) % 26 + 97)
            i += 1
        else:
            plain_text += j
    return plain_text


def rail_fence_encrypt(plain_text: str, key: int) -> str:
    if key < 0:
        return None
    cipher_text = []
    text_len = len(plain_text)
    j = 0
    down = True
    for i in range(text_len):
        if j == 0:
            down = True
        elif j == key - 1:
            down = False
        try:
            cipher_text[j] += plain_text[i]
        except:
            cipher_text.append(plain_text[i])
        j += 1 if down else -1
    return "".join(cipher_text)


def rail_fence_decrypt(cipher_text: str, key: int) -> str:
    if key < 0:
        return None
    text_len = len(cipher_text)
    plain_text = [""] * text_len
    index = 0
    for i in range(key):
        j = i
        down = True
        while j < text_len:
            plain_text[j] = cipher_text[index]
            index += 1
            if i == 0 or i == key - 1:
                j += 2 * (key - 1)
            elif down:
                j += 2 * (key - i - 1)
                down = not down
            else:
                j += 2 * i
                down = not down
    return "".join(plain_text)


def generate_auto_key(message, key):
    i = 0
    while True:
        if len(key) == len(message):
            break
        if message[i] == " ":
            i += 1
        else:
            key += message[i]
            i += 1
    return key


def autokey_encrypt(message, key_new):
    cipher_text = ""
    i = 0
    for letter in message:
        if letter == " ":
            cipher_text += " "
        else:
            x = (dict1[letter] + dict1[key_new[i]]) % 26
            i += 1
            cipher_text += dict2[x]
    return cipher_text


def autokey_decrypt(cipher_text, key_new):
    or_txt = ""
    i = 0
    for letter in cipher_text:
        if letter == " ":
            or_txt += " "
        else:
            x = (dict1[letter] - dict1[key_new[i]] + 26) % 26
            i += 1
            or_txt += dict2[x]
    return or_txt


def main():
    while True:
        print("\nChoose an operation:")
        print("1. Caesar Cipher")
        print("2. Vigenere Cipher")
        print("3. Rail Fence Cipher")
        print("4. Autokey Cipher")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            text = input("Enter the text to encrypt/decrypt: ")
            shift = int(input("Enter the shift value for Caesar cipher: "))
            encrypted = caesar_encrypt(text, shift)
            decrypted = caesar_decrypt(encrypted, shift)
            print("Encrypted text:", encrypted)
            print("Decrypted text:", decrypted)
        elif choice == "2":
            text = input("Enter the text to encrypt/decrypt: ")
            key = input("Enter the key for Vigenere cipher: ")
            encrypted = vigenere_encrypt(text, key)
            decrypted = vigenere_decrypt(encrypted, key)
            print("Encrypted text:", encrypted)
            print("Decrypted text:", decrypted)
        elif choice == "3":
            text = input("Enter the text to encrypt/decrypt: ")
            key = int(input("Enter the number of rails for Rail Fence cipher: "))
            encrypted = rail_fence_encrypt(text, key)
            decrypted = rail_fence_decrypt(encrypted, key)
            print("Encrypted text:", encrypted)
            print("Decrypted text:", decrypted)
        elif choice == "4":
            text = input("Enter the text to encrypt/decrypt: ")
            key = input("Enter the key for Autokey cipher: ")
            key = key.upper()
            text = text.upper()
            key = generate_auto_key(text, key)
            encrypted = autokey_encrypt(text, key)
            decrypted = autokey_decrypt(encrypted, key)
            print("Encrypted text:", encrypted)
            print("Decrypted text:", decrypted)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
