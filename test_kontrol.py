import unittest
from kontrol import bos_degerler, tekrar_edenler
class BosDegerTesti(unittest.TestCase):
    def test_bos_hucreleri_sayar(self):
        satirlar = [
            {"ad": "Ali", "sehir": ""},
            {"ad": "", "sehir": "Urfa"},
            {"ad": "Ayşe", "sehir": "  "},
        ]
        self.assertEqual(bos_degerler(satirlar), {"sehir": 2, "ad": 1})

class TekrarTesti(unittest.TestCase):
    def test_tekrar_eden_satiri_bulur(self):
        satirlar = [{"ad": "Ali"}, {"ad": "Ayşe"}, {"ad": "Ali"}]
        self.assertEqual(tekrar_edenler(satirlar), [({"ad": "Ali"}, 2)])


if __name__ == "__main__":
    unittest.main()