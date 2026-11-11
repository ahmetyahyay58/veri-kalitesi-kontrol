import csv


def oku(yol):
    with open(yol, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def bos_degerler(satirlar):
    """Her sütunda kaç boş değer olduğunu döndürür."""
    sonuc = {}
    for satir in satirlar:
        for kolon, deger in satir.items():
            if deger is None or deger.strip() == "":
                sonuc[kolon] = sonuc.get(kolon, 0) + 1
    return sonuc



def tekrar_edenler(satirlar):
    """Birden fazla geçen satırları ve kaç kez geçtiklerini döndürür."""
    sayac = {}
    for satir in satirlar:
        anahtar = tuple(sorted(satir.items()))
        sayac[anahtar] = sayac.get(anahtar, 0) + 1
    return [(dict(a), n) for a, n in sayac.items() if n > 1]