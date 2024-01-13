substitution_binding = {chr(65 + i): i for i in range(26)}
substitution_binding.update({chr(97 + i): i for i in range(26)})


def caesar_encrypt(plain_text: str, key: int) -> str:
    if key < 0:
        return None
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
    if key < 0:
        return None
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
    key_len = len(key)
    if key_len == 0:
        return plain_text
    cipher_text = ""
    i = 0
    for j in plain_text:
        if j.isalpha():
            if j.isupper():
                cipher_text += chr(
                    (ord(j) + substitution_binding[key[i % key_len]] - 65) % 26 + 65
                )
            else:
                cipher_text += chr(
                    (ord(j) + substitution_binding[key[i % key_len]] - 97) % 26 + 97
                )
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
                plain_text += chr(
                    (ord(j) - substitution_binding[key[i % key_len]] - 39) % 26 + 65
                )
            else:
                plain_text += chr(
                    (ord(j) - substitution_binding[key[i % key_len]] - 71) % 26 + 97
                )
            i += 1
        else:
            plain_text += j
    return plain_text


def rain_fence_encrypt(plain_text: str, key: int) -> str:
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


def rain_fence_decrypt(cipher_text: str, key: int) -> str:
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


import numpy as np


def prepare_text(text, block_size):
    # Convert to uppercase
    text = text.upper()

    # Replace non-alphabetic characters
    text = "".join(char for char in text if char.isalpha())

    # Padding if needed
    if len(text) % block_size != 0:
        text += "X" * (block_size - len(text) % block_size)

    return text


def text_to_matrix(text, block_size):
    # Convert text to matrix
    matrix = [substitution_binding[char] for char in text]
    return np.array(matrix).reshape(-1, block_size)


def matrix_to_text(matrix):
    # Convert matrix to text
    return "".join([chr(char + ord("A")) for row in matrix for char in row])


def mod_inverse(matrix, modulo):
    # Find the modular inverse of a matrix
    det = int(np.round(np.linalg.det(matrix))) % modulo
    det_inv = pow(det, -1, modulo)
    adjugate = np.round(det_inv * np.linalg.inv(matrix)).astype(int) % modulo
    return (det_inv * adjugate) % modulo


def encrypt_hill(plain_text, key_matrix):
    block_size = len(key_matrix)
    plain_text = prepare_text(plain_text, block_size)
    plain_matrix = text_to_matrix(plain_text, block_size)

    # Encrypt each block
    cipher_matrix = np.dot(plain_matrix, key_matrix) % 26

    # Convert the result to ciphertext
    cipher_text = matrix_to_text(cipher_matrix)

    return cipher_text


def decrypt_hill(cipher_text, key_matrix):
    block_size = len(key_matrix)
    cipher_text = prepare_text(cipher_text, block_size)
    cipher_matrix = text_to_matrix(cipher_text, block_size)

    # Calculate the modular inverse of the key matrix
    key_matrix_inv = mod_inverse(key_matrix, 26)

    # Decrypt each block
    plain_matrix = np.dot(cipher_matrix, key_matrix_inv) % 26

    # Convert the result to plaintext
    plain_text = matrix_to_text(plain_matrix)

    return plain_text


# Example usage
key = "HILLMAGIC"
plain_text = "GFG"

# Encryption
encrypted_text = encrypt_hill(plain_text, key)
print("Encrypted:", encrypted_text)

# Decryption
decrypted_text = decrypt_hill(encrypted_text, key)
print("Decrypted:", decrypted_text)
