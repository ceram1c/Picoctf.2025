import base64
import hashlib

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]

def decrypt(ciphertext, key):
    block_size = 16
    key_hash = hashlib.sha256(key).digest()
    plaintext = b''

    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i + block_size]
        plaintext_block = xor_bytes(block, key_hash)
        plaintext += plaintext_block

    return unpad(plaintext)

# Encrypted blockchain from your output
encrypted_blockchain = b''

# Key from your output
key = b''

# Decrypt the blockchain
decrypted_blockchain = decrypt(encrypted_blockchain, key)

# Decode the decrypted blockchain string
decoded_blockchain = decrypted_blockchain.decode('utf-8')

print("Decrypted Blockchain:", decoded_blockchain)