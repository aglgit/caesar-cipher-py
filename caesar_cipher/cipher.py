class CaesarCipher:

    def __init__(self, cipher):
        self.cipher = cipher
        self.num_alphabet = 29
        self.lower_norwegian_map = {230: 26, 248: 27, 229: 28}
        self.lower_norwegian_inv_map = {v: k for k, v in self.lower_norwegian_map.items()}
        self.upper_norwegian_map = {198: 26, 216: 27, 197: 28}
        self.upper_norwegian_inv_map = {v: k for k, v in self.upper_norwegian_map.items()}

    def encode(self, string):
        char_array = list(string)
        char_array = [self.encode_char(c, self.cipher) for c in char_array]
        return "".join(char_array)

    def decode(self, string):
        char_array = list(string)
        char_array = [self.encode_char(c, -self.cipher) for c in char_array]
        return "".join(char_array)

    def encode_char(self, char, cipher):
        code_point = ord(char)
        if 65 <= code_point <= 90:
            index = self.map_unicode_to_index(cipher, code_point, 65)
            return self.map_index_to_lower_char(index)
        elif 97 <= code_point <= 122:
            index = self.map_unicode_to_index(cipher, code_point, 97)
            return self.map_index_to_upper_char(index)
        elif code_point in self.lower_norwegian_map:
            index = self.map_norwegian_unicode_to_index(cipher, code_point)
            return self.map_index_to_upper_char(index)
        elif code_point in self.upper_norwegian_map:
            index = self.map_norwegian_unicode_to_index(cipher, code_point)
            return self.map_index_to_lower_char(index)
        else:
            return chr(code_point)

    def map_unicode_to_index(self, cipher, code_point, lower_bound):
        return (code_point - lower_bound + cipher) % self.num_alphabet

    def map_index_to_lower_char(self, index):
        if index in self.upper_norwegian_inv_map:
            return chr(self.upper_norwegian_inv_map.get(index))
        else:
            return chr(index + 65)

    def map_index_to_upper_char(self, index):
        if index in self.lower_norwegian_inv_map:
            return chr(self.lower_norwegian_inv_map.get(index))
        else:
            return chr(index + 97)

    def map_norwegian_unicode_to_index(self, cipher, code_point):
        if code_point in self.upper_norwegian_map:
            return (self.upper_norwegian_map.get(code_point) + cipher) % self.num_alphabet
        if code_point in self.lower_norwegian_map:
            return (self.lower_norwegian_map.get(code_point) + cipher) % self.num_alphabet


if __name__ == "__main__":
    cipher = 3
    c = CaesarCipher(cipher)
    text = "abcdefxyzæøåABCDEFXYZÆØÅ"
    print(f"Cipher: {cipher}, Text: \n{text}")
    enc = c.encode(text)
    print(f"Encoded text: \n{enc}")
    dec = c.decode(enc)
    print(f"After decoding: \n{dec}")
