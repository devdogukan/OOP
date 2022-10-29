def fonk_isim_yas_yaz(isim, yas):
    print(f'isim {isim}, yas: {yas}')
    
def fonk_isim_yas_sinif_yaz(isim = 'girilmedi', yas = 'girilmedi', sinif = 'girilmedi'):
    print(f'isim {isim}, yas: {yas}, sinif: {sinif}')
    
fonk_isim_yas_yaz(yas=13, isim='ali')

fonk_isim_yas_sinif_yaz()
fonk_isim_yas_sinif_yaz(sinif=3)
fonk_isim_yas_sinif_yaz(sinif=2, isim= 'Ali')