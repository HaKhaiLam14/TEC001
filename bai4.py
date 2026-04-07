def caesar_cipher_file(filename, shift, direction):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()

        result = ""

        if direction.lower() == "left":
            shift = -shift

        for c in text:
            if c.isupper():
                x = ord(c) - ord('A')
                y = (x + shift) % 26
                result += chr(y + ord('A'))

            elif c.islower():
                x = ord(c) - ord('a')
                y = (x + shift) % 26
                result += chr(y + ord('a'))

            else:
                result += c

        with open("ciphertext.txt", 'w', encoding='utf-8') as f:
            f.write(result)

        return "Encryption complete. Saved to ciphertext.txt"

    except:
        return "Error processing file"


file = input("Enter file name: ")
shift = int(input("Enter shift value: "))
direction = input("Enter direction (left/right): ")

print(caesar_cipher_file(file, shift, direction))