def encrypt_message(message, shift, alphabet):
    encrypted_message = "".join(alphabet[alphabet.index(char)+shift] if char in alphabet else char for char in message)
    return encrypted_message


def desencrypt_message(message, shift, alphabet):
    encrypted_message = "".join(alphabet[alphabet.index(char)-shift] if char in alphabet else char for char in message)
    return encrypted_message