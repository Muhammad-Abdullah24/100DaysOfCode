def rail_fence_cipher(text, key):

    rail = [[" " for i in range(len(text))] for j in range(key)]

    down = False
    row = 0
    col = 0

    for char in text:
        if row == 0 or row == key - 1:
            down = not down

        rail[row][col] = char
        col += 1

        if down:
            row += 1
        else:
            row -= 1

    cipher_text = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != " ":
                cipher_text.append(rail[i][j])

    return "".join(cipher_text)


def rail_fence_decipher(cipher_text, key):

    rail = [['\n' for i in range(len(cipher_text))] for j in range(key)]

    down = None
    row, col = 0, 0

    for i in range(len(cipher_text)):
        if row == 0:
            down = True
        if row == key - 1:
            down = False

        rail[row][col] = '*'
        col += 1

        row += 1 if down else -1

    index = 0
    for i in range(key):
        for j in range(len(cipher_text)):
            if rail[i][j] == '*' and index < len(cipher_text):
                rail[i][j] = cipher_text[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher_text)):
        if row == 0:
            down = True
        if row == key - 1:
            down = False

        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1

        row += 1 if down else -1

    return "".join(result)

def rail_fence_decrypt_brute_force(cipher_text):
    for key in range(2, (len(cipher_text) // 2) + 1):
        print(f"Decrypted message: {rail_fence_decipher(cipher_text, key)}")


# Example usage
plain1 = "ABDULLAH"
key = 3

plain2 = "CRYPTOGRAPHY"
key2 = 4
print("Test Case 1: ")
rail_fence_decrypt_brute_force(rail_fence_cipher(plain1, key))
print("Test Case 2: ")
rail_fence_decrypt_brute_force(rail_fence_cipher(plain2, key2))
