def topla(*args):
    return sum(args)

def carp(*args):
    carpim = 1
    for arg in args:
        carpim *= arg
    return carpim

def ortalama(*args):
    if len(args) == 0:
        return 0
    return topla(*args)/len(args)

def islem_yap(islem_adi):
    if islem_adi == "toplama":
        return topla
    if islem_adi == "carp":
        return carp
    if islem_adi == "ortalama":
        return ortalama
    
islem_fonksiyonu = islem_yap("ortalama")
print(islem_fonksiyonu(1, 2, 3, 5))