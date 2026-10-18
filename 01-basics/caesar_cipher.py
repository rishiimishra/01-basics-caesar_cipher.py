# A simple Caesar Cipher script in Python

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift uppercase letters
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            # Shift lowercase letters
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Keep spaces and punctuation as they are
            result += char
    return result

def decrypt(text, shift):
    # Decryption is just reversing the shift
    return encrypt(text, -shift)

# Test the program
secret_message = "Attack at Dawn"
key = 3

encrypted = encrypt(secret_message, key)
decrypted = decrypt(encrypted, key)

print(f"Original : {secret_message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
