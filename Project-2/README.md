# Project 2: Basic Encryption & Decryption (Caesar Cipher)

**DecodeLabs Cyber Security Internship — 2026 Batch**

## Overview
This project implements a simple, reversible encryption technique (the Caesar Cipher) to demonstrate the fundamentals of data confidentiality: turning readable plaintext into unreadable ciphertext, and reliably reversing that process back to plaintext.

## Goal
Implement a basic encryption and decryption technique that:
- Encrypts user text using a Caesar cipher (letter-shift logic)
- Decrypts the encrypted text back to the original
- Displays both the encrypted and decrypted output

## How It Works
1. Each letter is converted to its ASCII value using `ord()`.
2. The shift key `n` is added to that value.
3. `% 26` wraps the result around so it stays within the alphabet.
4. The result is converted back to a character using `chr()`.
5. Decryption reverses the process by subtracting the shift key instead of adding it.

Formulas:
```
Encryption: E(x) = (x + n) % 26
Decryption: D(x) = (x - n) % 26
```

Non-alphabet characters (spaces, numbers, punctuation) are passed through unchanged.

## Files
- `caesar_cipher.py` — the core implementation with `encrypt()`, `decrypt()`, and a command-line interface.

## Requirements
- Python 3.x (no external libraries needed)

## Usage
```bash
python3 caesar_cipher.py
```
You will be prompted to:
1. Enter the text you want to encrypt
2. Enter a shift key (any integer, e.g. `3`)

The program then prints the original text, the shift key, the encrypted text, and the decrypted text, and confirms whether the decrypted text matches the original.

### Example
```
Enter the text to encrypt: Hello, DecodeLabs! 123
Enter shift key (e.g. 3): 3

--- Results ---
Original text : Hello, DecodeLabs! 123
Shift key     : 3
Encrypted text: Khoor, GhfrghOdev! 123
Decrypted text: Hello, DecodeLabs! 123

[OK] Decryption matches the original message.
```

## Key Skills Demonstrated
- Encryption/decryption concepts
- Logic building with modular arithmetic
- Data protection basics (handling edge cases like case sensitivity and non-alphabet characters)


## Author
DecodeLabs Cyber Security Trainee — Project 2 Submission