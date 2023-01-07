from musteri import Musteri
from yemek import Yemek

kuru = Yemek('kuru fasulye',25)
pilav = Yemek('pilav',20)
cacik = Yemek('cacik',15)
tatli = Yemek('baklava',60)
nohut = Yemek('nohut',30)
kebab = Yemek('kebab',80)
m1 = Musteri('elif','aslan',200,'osmaniye','merkez') 
m2 = Musteri('mehmet','sakin',150,'adana','seyhan') 

m1.siparis_ekle(kuru)
m2.siparis_ekle(kebab)
m1.siparis_ekle(pilav)
m2.siparis_ekle(tatli)
m1.siparis_ekle(cacik)

print(m1)
print(m2)


"""
örnek çıktı:
ad:elif,soyad:aslan,bakiye140
adres:osmaniye-merkez
*yemek:kuru fasulye,25tl
*yemek:pilav,20tl
*yemek:cacik,15tl

ad:mehmet,soyad:sakin,bakiye10
adres:adana-seyhan
*yemek:kebab,80tl
*yemek:baklava,60tl

"""