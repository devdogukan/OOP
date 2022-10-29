from banka1 import Hesap

kisi1 =  Hesap('Yusuf', 'Kanmaz',220)
kisi2 = Hesap('Fatma', 'Demir',500)
kisi1.dokum()
try:
    kisi1.bakiye = 50 
except Exception as e:
    print(str(e)) 
kisi1.ad = 'Hasan'
kisi1.yatir(35) 
kisi1.harca('Market',58)
kisi2.harca('Kuafor',350)
kisi1.harca('Kasap',100)
try:
    kisi1.yatir(-20)
except Exception as e:
    print(str(e))
try:
    kisi2.harca('Çanta',480)
except Exception as e:
    print(str(e))
kisi1.harca('Fatura',80)
kisi1.dokum()
kisi2.dokum()


"""
örnek çıktı
--------------------
Yus***,Kan***
*Başlangıç bakiyesi,220
Hesap Bakiyesi:220
--------------------
Bakiye değiştirilemez!
Yatırılan miktar 0'dan büyük olmalıdır!
Bakiye yetersiz!
--------------------
Has***,Kan***
*Başlangıç bakiyesi,220
*Para Yatırma,35
*Market,-58
*Kasap,-100
*Fatura,-80
Hesap Bakiyesi:17
--------------------
--------------------
Fat***,Dem***
*Başlangıç bakiyesi,500
*Kuafor,-350
Hesap Bakiyesi:150
--------------------
"""