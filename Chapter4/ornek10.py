def altini_ciz(cagrilacak_fonksiyon, *args):
    cagrilacak_fonksiyon(*args)
    print('-'*30)
    
def bilgi_yaz(*args):
    for arg in args:
        print(arg)
        
altini_ciz(bilgi_yaz, "ali", "yilmaz", "ybs", 3)
altini_ciz(bilgi_yaz)
altini_ciz(bilgi_yaz, "ayse")
altini_ciz()
