def bilgi_yaz(bilgi):
    def isim_yaz(isim):
        print(f'isim: {isim}')
        
    def soy_isim_yaz(soy_isim):
        print(f'soyisim: {soy_isim}')
        
    def yas_yaz(yas):
        print(f'yas: {yas}')
    
    yer_tutucu = None
    if bilgi == 'isim':
        yer_tutucu = isim_yaz
    elif bilgi == 'soyisim':
        yer_tutucu = soy_isim_yaz
    elif bilgi == 'yas':
        yer_tutucu = yas_yaz
        
    return yer_tutucu   # return ***********************
    
degisken1 = bilgi_yaz("isim")
degisken1('ali')