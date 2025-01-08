import math

class PythagoreanCryptography:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        self.c = math.sqrt(a**2 + b**2)
    
    def encrypt(self, plaintext: str) -> list:
        encrypted = []
        for char in plaintext:
            ascii_value = ord(char)
            x_prime = ascii_value * self.a
            y_prime = ascii_value * self.b
            encrypted.append((x_prime, y_prime))
        return encrypted

    def decrypt(self, encrypted: list) -> str:
        decrypted = ""
        for x_prime, y_prime in encrypted:
            ascii_value = x_prime // self.a
            decrypted += chr(ascii_value)
        return decrypted

    def encrypt_bytes(self, plaintext: str) -> bytes:
        encrypted = self.encrypt(plaintext)
        byte_array = []
        for x_prime, y_prime in encrypted:
            byte_array.extend([x_prime.to_bytes(4, 'big'), y_prime.to_bytes(4, 'big')])
        return b"".join(byte_array)

    def decrypt_bytes(self, encrypted_bytes: bytes) -> str:
        encrypted = []
        for i in range(0, len(encrypted_bytes), 8):
            x_prime = int.from_bytes(encrypted_bytes[i:i+4], 'big')
            y_prime = int.from_bytes(encrypted_bytes[i+4:i+8], 'big')
            encrypted.append((x_prime, y_prime))
        return self.decrypt(encrypted)
