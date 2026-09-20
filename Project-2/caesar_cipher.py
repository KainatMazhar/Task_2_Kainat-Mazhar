"""
Project 2: Basic Encryption & Decryption (Caesar Cipher)
DecodeLabs Cyber Security Internship

Implements:
    - encrypt(text, shift): converts plaintext -> ciphertext
    - decrypt(text, shift): converts ciphertext -> plaintext
    - A simple CLI that displays both encrypted and decrypted output
"""


def encrypt(text: str, shift: int) -> str:
    result = []
    for char in text:
        if char.isupper():
            base = ord('A')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        elif char.islower():
            base = ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)


def decrypt(text: str, shift: int) -> str:
    return encrypt(text, -shift)


def main():
    print("=== DecodeLabs Caesar Cipher Tool ===")
    message = input("Enter the text to encrypt: ")

    while True:
        try:
            shift = int(input("Enter shift key (e.g. 3): "))
            break
        except ValueError:
            print("Please enter a whole number for the shift key.")

    encrypted = encrypt(message, shift)
    decrypted = decrypt(encrypted, shift)

    print("\n--- Results ---")
    print(f"Original text : {message}")
    print(f"Shift key     : {shift}")
    print(f"Encrypted text: {encrypted}")
    print(f"Decrypted text: {decrypted}")

    if decrypted == message:
        print("\n[OK] Decryption matches the original message.")
    else:
        print("\n[ERROR] Decryption does NOT match the original message.")


if __name__ == "__main__":
    main()      