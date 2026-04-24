# =========================================
# Project 2: Caesar Cipher Tool
# Description: Encrypts and decrypts text
# using shift-based cryptographic logic
# =========================================

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result


def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char
    return result


def get_shift():
    while True:
        try:
            shift = int(input("Enter shift value: "))
            return shift % 26
        except ValueError:
            print("❌ Invalid input. Please enter a number.")


def main():
    print("\n🔐 Caesar Cipher Tool")
    print("======================")

    while True:
        print("\nChoose an option:")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            text = input("Enter text to encrypt: ")
            shift = get_shift()
            encrypted = encrypt(text, shift)
            print("\n✅ Encrypted Text:", encrypted)

        elif choice == "2":
            text = input("Enter text to decrypt: ")
            shift = get_shift()
            decrypted = decrypt(text, shift)
            print("\n✅ Decrypted Text:", decrypted)

        elif choice == "3":
            print("👋 Exiting program. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")


# Run program
if __name__ == "__main__":
    main()