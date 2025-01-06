
class CaesarCipher:

    def __init__(self, cipher):
        self.cipher = cipher

    def encode_char(self, char):
        code_point = ord(char)
        lower_dict = {230: 26, 248: 27, 229: 28}
        upper_dict = {198: 26, 216: 27, 197: 28}
        inv_lower = {v: k for k, v in lower_dict.items()}
        inv_upper = {v: k for k, v in upper_dict.items()}
        if code_point >= 65 and code_point <= 90:
            r = (code_point - 65 + self.cipher ) %29
            if r in inv_upper:
                return chr(inv_upper.get(r))
            else:
                return chr( r +65)
        elif code_point >= 97 and code_point <= 122:
            r = (code_point - 97 + self.cipher ) %29
            if r in inv_lower:
                return chr(inv_lower.get(r))
            else:
                return chr( r +97)
        elif code_point in lower_dict:
            r = (lower_dict.get(code_point) + self.cipher ) %29
            if r in inv_lower:
                return chr(inv_lower.get(r))
            else:
                return chr( r +97)
        elif code_point in upper_dict:
            r = (upper_dict.get(code_point) + self.cipher ) %29
            if r in inv_upper:
                return chr(inv_upper.get(r))
            else:
                return chr( r +65)
        else:
            return chr(code_point)

    def encode(self, string):
        char_array = list(string)
        char_array = [self.encode_char(c) for c in char_array]
        return "".join(char_array)

    def decode(self, string):
        char_array = list(string)
        char_array = [self.to_char(self.to_unicode(c) - self.cipher)
                      for c in char_array]
        return "".join(char_array)


if __name__ == "__main__":
    c = CaesarCipher(3)
    res = c.encode2("abcdef")
    print(res)
