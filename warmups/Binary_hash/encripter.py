import binary_hash
b_hash = binary_hash.binary_hash
print(b_hash)


def encrypt(message):
    ans = []
    message = lists(message)
    for letter in message:
        letter = b_hash[letter]
        ans.append(letter)

    ans = ''.join(ans)
    print(ans)
encrypt('hello')
