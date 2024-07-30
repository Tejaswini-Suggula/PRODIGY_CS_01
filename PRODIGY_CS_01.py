def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    choice = input("Do you want to encrypt or decrypt? (e/d): ").strip().lower()
    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
        return

    text = input("Enter the message: ").strip()
    shift = int(input("Enter the shift value: ").strip())

    if choice == 'e':
        result = encrypt(text, shift)
        print(f"Encrypted message: {result}")
    else:
        result = decrypt(text, shift)
        print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
