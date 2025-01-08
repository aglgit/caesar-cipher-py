from unittest import TestCase

from caesar_cipher import CaesarCipher


class TestCaesarCipher(TestCase):
    def test_encode(self):
        cipher = CaesarCipher(3)
        text = "abcdef xyzæøå ABCDEFXYZ ÆØÅ"
        self.assertEquals("defghi æøåabc DEFGHIÆØÅ ABC", cipher.encode(text))

    def test_decode(self):
        cipher = CaesarCipher(3)
        text = "defghi æøåabc DEFGHIÆØÅ ABC"
        self.assertEquals("abcdef xyzæøå ABCDEFXYZ ÆØÅ", cipher.decode(text))

    def test_encode_then_decode(self):
        cipher = CaesarCipher(3)
        text = "defghi æøåabc DEFGHIÆØÅ ABC"
        self.assertEquals(text, cipher.decode(cipher.encode(text)))
