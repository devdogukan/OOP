"""
ad soyad = Doğukan AKSOY
numara = 20217170050
"""


class Hesap: 
    """Hesap ve harcama bilgilerini tutan sınıf"""
    harcanan_miktar:int = 0
    yatirilan_miktar:int = 0

    def __init__(self,ad,soyad,baslangic_bakiyesi) -> None:
        """Hesap Constructor
        Args:
            ad (str): kişi adı
            soyad (str): kişi soyadı
            baslangic_bakiyesi (str): hesap açılış bakiyesi
        """ 
        self._ad = ad
        self._soyad = soyad
        self._baslangic_bakiyesi = baslangic_bakiyesi
        self.hareket = []
        self.aciklama = []

    @property
    def ad(self):
        """ad property getter
        Returns:
            str: adın ilk üç harfi ve 3 yıldız
            örnek: Ayş***
        """ 
        return f'{self._ad[:3]}***'
    
    @ad.setter
    def ad(self,value):
        """ad setter
        Args:
            value (str): kişi adı
        """ 
        self._ad = value
 
    @property
    def soyad(self):
        """soyad setter
        Returns:
            str: soyadın ilk üç harfi ve 3 yıldız
            örnek: Yıl***
        """ 
        return f'{self._soyad[:3]}***'
 
    @soyad.setter
    def soyad(self,value):
        """soyad setter
        Args:
            value (str): kişi soyadı
        """ 
        self._soyad = value
 
    @property
    def bakiye(self):
        """bakiye property
        Returns:
            float: kişi bakiyesi
        """ 
        return self._baslangic_bakiyesi + self.yatirilan_miktar - self.harcanan_miktar
 
    @bakiye.setter
    def bakiye(self,value):
        """bakiye setter
        Args:
            value (float): bakiye property si read-only dir
        Raises:
            AttributeError: Bakiye değiştirilemez!
        """ 
        raise AttributeError("Bakiye değiştirilemez!")

    def __hareket_ekle(self,aciklama,miktar):
        """hareket ekle methodu
        Args:
            aciklama (str): hareket açıklaması
            miktar (float): miktar 
        """ 
        self.hareket.append(miktar)
        self.aciklama.append(aciklama)

    def yatir(self,value):
        """para yatirma methodu
        Args:
            value (float): yatan miktar
        miktar negatif olursa aşağıdaki hata gerçekleşmelidir.
        Raises:
            AttributeError: Yatırılan miktar 0'dan büyük olmalıdır!
        """ 
        if value <= 0:
            raise AttributeError("Yatırılan miktar 0'dan büyük olmalıdır!")
        
        self.yatirilan_miktar += value
        self.__hareket_ekle('Para Yatırma', value)

    def harca(self,aciklama,miktar):
        """harcama methodu
        Args:
            aciklama (str): harcama açıklaması
            miktar (float): miktar
            miktar negatif olursa aşağıdaki hata gerçekleşir
        Raises:
            AttributeError: Harcanan miktar 0'dan büyük olmalıdır!
        
            miktar bakiyeden büyük olursa aşağıdaki hata gerçekleşir
        Raises:
            AttributeError: Bakiye yetersiz!
        """ 
        if miktar <= 0:
            raise AttributeError("Harcanan miktar 0'dan büyük olmalıdır!")
        elif miktar > self.bakiye:
            raise AttributeError("Bakiye yetersiz!")
        
        self.harcanan_miktar += miktar
        self.__hareket_ekle(aciklama, -miktar)
        

    def dokum(self):
        """hesap dokumu methodu 
        önce ------ yazar 20 çizgi
        sonra kişinin adı ve soyadı yazar
        sonra tüm hareketler alt alta yazılır
        sonra hesap bakiyesi yazılır
        sonra ------ yazar 20 çizgi
        
        """
        print("-"*20)
        print(f'{self.ad},{self.soyad}')
        print(f'*Başlangıç bakiyesi,{self._baslangic_bakiyesi}')
        for k in range(len(self.hareket)):
            print(f'*{self.aciklama[k]},{self.hareket[k]}')
        print(f'Hesap Bakiyesi:{self.bakiye}')
        print('-'*20)
        