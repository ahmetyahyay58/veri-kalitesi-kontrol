import unittest
from kontrol import bos_degerler


class BosDegerTesti(unittest.TestCase):
    def test_bos_hucreleri_sayar(self):
        satirlar = [
            {"ad": "Ali", "sehir": ""},
            {"ad": "", "sehir": "Urfa"},
            {"ad": "Ayşe", "sehir": "  "},
        ]
        self.assertEqual(bos_degerler(satirlar), {"sehir": 2, "ad": 1})


if __name__ == "__main__":
    unittest.main()