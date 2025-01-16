"""Arquivo que contém uma forma de descriptografar arquivos
Utilizando criptografia simétrica"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def descriptografar(user_key: str, dado_criptografado: bytes):
    """Descriptografando Arquivos atravéz de uma chave"""
    iv = dado_criptografado[:16]
    key = user_key.encode()
    dado_criptografado = dado_criptografado[16:]
    
    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend=default_backend()
    )

    decryptor = cipher.decryptor()

    dado_descriptografado = decryptor.update(dado_criptografado) + decryptor.finalize()
    
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    dado_original = unpadder.update(dado_descriptografado) + unpadder.finalize()
    
    return dado_original
