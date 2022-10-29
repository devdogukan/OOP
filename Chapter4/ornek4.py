def bilgileri_yaz(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
    print('bilgileri_yaz calisti') 

bilgileri_yaz()
bilgileri_yaz(isim='Ayse')
bilgileri_yaz(isim='Ali', yas=22, bolum='YBS')
bilgileri_yaz(plaka ='80ab001', model = 2022, marka = 'mercedes')