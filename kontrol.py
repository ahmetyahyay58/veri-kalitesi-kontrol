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