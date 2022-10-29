def fonk_topla(*args):
    toplam = 0
    for arg in args:
        toplam += arg
    print(f'toplam: {toplam}')
    
    
fonk_topla(1, 2, 3, 4, 5)