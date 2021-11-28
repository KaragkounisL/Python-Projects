import random

msg = "Hello World"
print(msg)
char_pool = ''
encryption_level = 128 // 8

for i in range(0x00, 0xFF):
    char_pool += chr(i)

key = ''
for i in range(encryption_level):
    key += random.choice(char_pool)

max_key_index = len(key) - 1


def encryption(msg):
    global max_key_index
    key_index = 0
    encrypted_msg = ''
    for char in msg:
        if key_index > max_key_index:
            key_index = 0
        encrypted_msg += chr(ord(char) ^ ord(key[key_index]))
        key_index += 1
    return encrypted_msg


def decryption(msg):
    key_index = 0
    global max_key_index
    decrypted_msg = ''
    for char in msg:
        if key_index > max_key_index:
            key_index = 0
        decrypted_msg += chr(ord(char) ^ ord(key[key_index]))
        key_index += 1
    return decrypted_msg


x = encryption(msg)
print(x)
print(decryption(x))
