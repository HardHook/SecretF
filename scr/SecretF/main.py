from cryptography.fernet import Fernet


class Full:

    def __init__(self):
        self.key = ''
        self.cipher = ''

    def secret(self):
        self.key = Fernet.generate_key()
        key = self.key
        return key

    def read(self):
        self.cipher = Fernet(self.key)
        with open('../../my_key.txt', 'wb') as f:
            f.write(self.key)
        text_to_secure = open('../../stih.txt', 'rb').read()
        return text_to_secure

    def reading(self, text_to_secure):
        with open('../../my_secured_text.txt', 'wb') as f:
            f.write(self.cipher.encrypt(text_to_secure))

    def end(self):
        text_to_unsecure = open('../../my_secured_text.txt', 'rb').read()
        with open('../../my_unsecured_text.txt', 'wb') as f:
            f.write(self.cipher.decrypt(text_to_unsecure))
        return text_to_unsecure
