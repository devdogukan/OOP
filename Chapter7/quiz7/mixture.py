"""
Name Surname = Doğukan AKSOY
Number = 20217170050

"""

class Mixture:
    """Salt and water mixture manipulation class"""

    def __init__(self, total_amount, salt_amount) -> None:
        """Mixture Constructor

        Args:
            total_amount (float): water + salt amount
            salt_amount (float): salt amount
        """
        self._total_amount = total_amount
        self._salt_amount  = salt_amount

    @property
    def salt_ratio(self):
        """salt_ratio property getter

        Returns:
            float: salt_amount / total_amount
        """
        return self._salt_amount / self._total_amount


    @salt_ratio.setter
    def salt_ratio(self, value):
        """salt_ratio property setter
        Calculates salt_amount with salt_ratio and total_amount 
        and sets salt_amount 

        Args:
            value (float): salt ratio
        """
        self._salt_amount = self._total_amount * value


    @property
    def water_amount(self):
        """water_amount property getter

        Returns:
            float: total_amount - salt_amount
        """   
        return self._total_amount - self._salt_amount


    @water_amount.setter
    def water_amount():
        """water_amount property setter
        water_amount is a calculated property 
        it is read-only

        Args:
            value (float): water amount (but not used)

        Raises:
            AttributeError: "Cannot set water amount"
        """
        raise AttributeError("Cannot set water amount")


    @property
    def water_ratio(self):
        """water_ratio property getter

        Returns:
            float: 1 - salt_ratio
        """
        return 1 - self.salt_ratio


    @water_ratio.setter
    def water_ratio():
        """water_ratio property setter
        water_ratio is a calculated property 
        it is read-only

        Args:
            value (float): water ratio (but not used)

        Raises:
            AttributeError: "Cannot set water ratio"
        """
        raise AttributeError("Cannot set water ratio")


    @classmethod
    def from_salt_ratio(cls, total_amount, salt_ratio):
        """from_salt_ratio is a classmethod 
        it is a alternative constructor
        it calls main constructor with total_amount and 0 salt_amount
        and creates a new instance
        it sets salt_ratio property of new instance

        Args:
            total_amount (float): water + salt amount
            salt_ratio (float): salt ratio

        Returns:
            Mixture: created new instance 
        """
        
        
        return cls(total_amount,total_amount*salt_ratio)


    @classmethod
    def from_water_ratio(cls, total_amount, water_ratio):
        """from_water_ratio is a classmethod 
        it is a alternative constructor
        it calls from_salt_ratio alternative constructor with total_amount and 1-water_ratio 

        Args:
            total_amount (float): water + salt amount
            water_ratio (float): water ratio

        Returns:
            Mixture: created new instance 
        """
        
        salt_ratio = 1 - water_ratio
        
        return cls(total_amount, total_amount*salt_ratio)


    @classmethod
    def from_water_amount(cls, total_amount, water_amount):
        """from_water_amount is a classmethod 
        it is a alternative constructor
        it calls main constructor with total_amount and total_amount-water_amount
        and creates a new instance 

        Args:
            total_amount (float): water + salt amount
            water_amount (float): water amount

        Returns:
            Mixture: created new instance 
        """
        
        return cls(total_amount, total_amount-water_amount)


    @classmethod
    def from_amounts(cls, water_amount, salt_amount):
        """from_amounts is a classmethod 
        it is a alternative constructor
        it calls main constructor with water_amount+salt_amount and salt_amount
        and creates a new instance 

        Args:
            water_amount (float): water amount
            salt_amount (float): salt amount

        Returns:
            Mixture: created new instance 
        """
        return cls(water_amount+salt_amount, salt_amount)


    def __add__(self, rhs):
        """Mixture class + operator overloader
        it creates a new instance with self.total_amount + rhs.total_amount and self.salt_amount + rhs.salt_amount


        Args:
            rhs (Mixture): right hand side object

        Returns:
            Mixture: created new instance
        """
        return Mixture(self._total_amount + rhs._total_amount, self._salt_amount + rhs._salt_amount)


    def __truediv__ (self, value):
        """Mixture class / operator overloader
        it creates a new instance with self.total_amount / value and self.salt_amount / value


        Args:
            value (float): divider

        Returns:
            Mixture: created new instance
        """
        
        return Mixture(self._total_amount/value, self._salt_amount/value)


    def __mul__(self, value):
        """Mixture class * operator overloader
        it creates a new instance with self.total_amount * value and self.salt_amount * value


        Args:
            value (float): multiplier

        Returns:
            Mixture: created new instance
        """
        
        return Mixture(self._total_amount*value, self._salt_amount*value)


    def __eq__(self, rhs) -> bool:
        """Mixture class == operator overloader

        Args:
            rhs (Mixture): right hand side object

        Returns:
            bool: self.total_amount == rhs.total_amount and self.salt_amount == rhs.salt_amount
        """
        
        return self._total_amount == rhs._total_amount and self._salt_amount == rhs._salt_amount

        

    def __str__(self) -> str:
        """Mixture class to string method overloader

        Returns:
            str: 'SA:{:3.2f},WA:{:3.2f},SR:{:3.2f},WR:{:3.2f},TOTAL:{:3.2f}'
        """
        
        return f'SA:{self._salt_amount:3.2f},WA:{self.water_amount:3.2f},SR:{self.salt_ratio:3.2f},WR:{self.water_ratio:3.2f},TOTAL:{self._total_amount:3.2f}'


    
