def encrypt_text(text, shift):
    encrypted = ""

    for char in text:
        if char.isalpha():

            if char.isupper():
                encrypted += chr((ord(char) - 65 + shift) % 26 + 65)

            else:
                encrypted += chr((ord(char) - 97 + shift) % 26 + 97)

        else:
            encrypted += char

    return encrypted


def decrypt_text(text, shift):
    decrypted = ""

    for char in text:
        if char.isalpha():

            if char.isupper():
                decrypted += chr((ord(char) - 65 - shift) % 26 + 65)

            else:
                decrypted += chr((ord(char) - 97 - shift) % 26 + 97)

        else:
            decrypted += char

    return decrypted


try:
    with open("sample.txt", "r") as file:
        content = file.read()

    encrypted_content = encrypt_text(content, 3)

    print("Original Content:")
    print(content)

    print("\nEncrypted Content:")
    print(encrypted_content)

    with open("encrypted_sample.txt", "w") as file:
        file.write(encrypted_content)

    print("\nEncrypted file created successfully.")
    with open("encrypted_sample.txt", "r") as file:
        encrypted_file_content = file.read()

    decrypted_content = decrypt_text(encrypted_file_content, 3)

    with open("decrypted_sample.txt", "w") as file:
        file.write(decrypted_content)

    print("\nDecrypted file created successfully.")

except FileNotFoundError:
    print("sample.txt file not found.")