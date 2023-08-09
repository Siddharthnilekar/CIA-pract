from Crypto.Cipher import AES

key = b'C&F)H@McQfTjWnZr'
cipher = AES.new(key, AES.MODE_EAX)
data = input("Enter your plain text: ").encode()
nonce = cipher.nonce
ciphertext = cipher.encrypt(data)
print("Cipher text:", ciphertext)

cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
print("Plain text:", plaintext)