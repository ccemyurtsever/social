import base64

def encrypt(text):
    text_bytes = text.encode('utf-8')
    encrypted_bytes = base64.b64encode(text_bytes)
    encrypted_text = encrypted_bytes.decode('utf-8')
    return encrypted_text

def decrypt(encrypted_text):
    encrypted_bytes = encrypted_text.encode('utf-8')
    decrypted_bytes = base64.b64decode(encrypted_bytes)
    decrypted_text = decrypted_bytes.decode('utf-8')
    return decrypted_text

original_text = str(input())
encrypted_text = encrypt(original_text)
decrypted_text = decrypt(encrypted_text)
