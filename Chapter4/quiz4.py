import time

'''
Doğukan AKSOY
20217170050
2.Sinif Bil. Müh.

'''

def zaman_hesapla(fonk):
    def wrapper(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonk(*args, **kwargs)
        bitis  = time.time()
        print(f'islem {bitis - baslangic} saniye surdu')
        return sonuc
    return wrapper

@zaman_hesapla
def kareleri_al(liste):
    sonuc = []
    for i in liste:
        sonuc.append(i * i)
    return sonuc

@zaman_hesapla
def kupleri_al(liste):
    sonuc = []
    for i in liste:
        sonuc.append(i ** 3)
    return sonuc

@zaman_hesapla
def topla(*args):
    time.sleep(1)
    return sum(args)


print(kupleri_al(range(1000)))


# Ogrencinin testleri
print(kareleri_al(range(10)))
print(kupleri_al(range(10)))
print(topla(1, 2, 3, 4, 5, 6, 7, 8, 9))