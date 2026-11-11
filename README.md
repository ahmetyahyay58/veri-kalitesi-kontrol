# veri-kalitesi-kontrol

CSV dosyalarındaki boş ve tekrar eden satırları bulan küçük bir Python aracı.

## Kullanım

    from kontrol import oku, bos_degerler, tekrar_edenler

    satirlar = oku("veri.csv")
    print(bos_degerler(satirlar))
    print(tekrar_edenler(satirlar))

## Test

    python -m unittest