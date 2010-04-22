from ecomstore.settings import CURRENT_PATH
from keyczar import keyczar
import os

KEY_PATH = os.path.join(CURRENT_PATH, 'keys')

def encrypt(plaintext):
    crypter = _get_crypter()
    return crypter.Encrypt(plaintext)

def decrypt(ciphertext):
    crypter = _get_crypter()
    return crypter.Decrypt(ciphertext)

def _get_crypter():
    return keyczar.Crypter.Read(KEY_PATH)