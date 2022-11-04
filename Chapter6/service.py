"""Quiz 6
Numara: 20217170050
Ad Soyad: Doğukan AKSOY
"""

from datetime import date 

class Service:
    """Tamir servisi işlemlerini yapan sınıf"""

    """işçilik ücreti oranını ve servisin adını class variable olarak tanımlayıp, 
    ilk değerlerini giriniz. """ 


    """ price_list dictionary'si class variable olarak tanımlanmıştır
        üzerinde herhangi bir değişiklik yapmayınız
        yapılan işlemin ücretini hesaplamak için faydalanmalısınız.
    """
    workmanship_rate = 0
    service_name = ""
    total_price = 0
    
    price_list = {
        "yag":400,
        "yag_filtresi":75,
        "hava_filtresi":110,
        "polen_filtresi":60,
        "yikama":50,
        "motor_temizligi":100,
        "buji":600,
        "aku":1500,
        "balata":750,
        "disk":1600,
        "triger":1250,
    }

    def __init__(self, plate_no:str, name_surname:str, work_list=[]) -> None:
        """Service constructor

        Args:
            plate_no (str): plaka no
            name_surname (str): isim soyisim
            work_list (list[str]): yapılacak iş listesi
        """
        self.plate_no = plate_no
        self._name_surname = name_surname
        self.work_list = work_list
        self.do = []


    @classmethod
    def onbin(cls,plate_no:str, name_surname:str, work_list=[]):
        """onbin bakımı için ön tanımlı iş listesine sahip constructor overload

        Args:
            plate_no (str): plaka no
            name_surname (str): isim soyisim
            work_list (list[str], optional): yapılacak iş listesi varsayılan değeri [].

        ön tanımlı iş listesi["yag","yag_filtresi","hava_filtresi","polen_filtresi","yikama"]
        Returns:
            Service: geriye service türünde bir örnek döndürüyor
        """
        work_list.extend(["yag","yag_filtresi","hava_filtresi","polen_filtresi","yikama"])
        return cls(plate_no, name_surname, work_list)
        
    
    @classmethod
    def yirmibin(cls,plate_no:str, name_surname:str, work_list=[]):
        """yirmibin bakımı için ön tanımlı iş listesine sahip constructor overload

        Args:
            plate_no (str): plaka no
            name_surname (str): isim soyisim
            work_list (list[str], optional): yapılacak iş listesi varsayılan değeri [].

        ön tanımlı iş listesi["motor_temizligi","balata","disk","yag","yag_filtresi","hava_filtresi","polen_filtresi","yikama"]
        Returns:
            Service: geriye service türünde bir örnek döndürüyor
        """ 
        work_list = ["motor_temizligi","balata","disk"]
        return cls.onbin(plate_no, name_surname, work_list)
    
    @classmethod
    def otuzbin(cls,plate_no:str, name_surname:str, work_list=[]):
        """otuzbin bakımı için ön tanımlı iş listesine sahip constructor overload

        Args:
            plate_no (str): plaka no
            name_surname (str): isim soyisim
            work_list (list[str], optional): yapılacak iş listesi varsayılan değeri [].

        ön tanımlı iş listesi["triger","buji","motor_temizligi","balata","disk","yag","yag_filtresi","hava_filtresi","polen_filtresi","yikama"]
        Returns:
            Service: geriye service türünde bir örnek döndürüyor
        """ 
        work_list = ["motor_temizligi","balata","disk","yag","yag_filtresi","hava_filtresi","polen_filtresi","yikama"]
        return cls(plate_no, name_surname, work_list)
    
    @property
    def name_surname(self) -> str:
        """name_surname getter

        Returns:
            str: __name ve __surname gizli değişkenlerinde tutulan anonimleştirilmiş isim ve soy ismi geriye döndürür
            örnek: Ala*** Uça***
        """ 
        return Service.anonymize(self._name_surname)

    @name_surname.setter
    def name_surname(self,value:str) -> None:
        """name_surname setter

        Args:
            value (str): içerisine isim ve soyisim alıyor ve __name ve __surname gizli değişkenlerine atama yapıyor.
        """ 
        self._name_surname = value

    @classmethod
    def set_workmanship_rate(cls,workmanship_rate:float) -> None:
        """işçilik oranı class variable ını değiştiren class method

        Args:
            workmanship_rate (float): işçilik oranı
        """ 
        cls.workmanship_rate = workmanship_rate

    @classmethod
    def set_service_name(cls,service_name) -> None:
        """servis adı class variable nı değiştiren class method

        Args:
            service_name (_type_): servis adı 
        """ 
        cls.service_name = service_name

    def do_worklist(self):
        """iş listesinde yer alan her işçilik kalemi için
           önce işin fiyatını bulur
           sonra işçilik oranına göre işçilik ücretini hesaplar
           yapılan işler listesine ekler
        """ 
        for work in self.work_list:
            self.do.append(f"*{work},{self.price_list[work]}tl,{self.price_list[work]*self.workmanship_rate}tl")
            self.total_price += self.price_list[work]
            self.total_price += self.price_list[work]*self.workmanship_rate
        

    def print(self) -> None:
        """serviste yapılan işlerin ücret özetini ekrana basar
        format:
            20 tane -
            <plaka>-<anonimleştirilmiş isim soy isim>-<bugünkü tarih, yıl,ay,gün>
            başında * ile yapılan her bir işlemi alt alta *<work>,<price>tl,<workmanship>tl
            İşçilik Oranı: <workmanship_rate>
            Toplam: <toplam_tutar>tl
            Servis: <service_name>
            20 tane -
        """ 
        
        print('-'*20)
        print(f"{self.plate_no}-{self.name_surname}-{date.today()}")
        for i in self.do:
            print(i)
        print(f"İşçilik Oranı:{self.workmanship_rate}")
        print(f"Toplam:{self.total_price}tl")
        print(f"Servis:{self.service_name}")
        print('-'*20)
        

    @staticmethod
    def anonymize(_in) -> str:
        """Gelen stringin ilk üç harfini alır ve 
        sonuna *** ekleyerek anonimleştirme işlemi gerçekleştirir.
        Bu bir static methoddur.

        Args:
            _in (str): gelen string

        Returns:
            str: anonimleşmiş string
        """ 
        
        name, surname = _in.split(" ")
        name = f"{name[0:3]}***"
        surname = f"{surname[0:3]}***"
        return f'{name} {surname}'
