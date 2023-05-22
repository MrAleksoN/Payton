class Passport:
    def __init__(self,country,name,surname,birth_date):
        self.contry=country
        self.name=name
        self.surname=surname
        self.birth_date=birth_date
    def print_info(self):
        print (self.country,self.name,self.surname,self.birth_date)

class foreignPassport(Passport):
    def __init__(self, country, name, surname, birth_date,visas,passport_number):
        super().__init__(country, name, surname, birth_date)
        self.passport_number='FA683389'
        self.visas=111
    def Print(self):
        super().print_info()
        print(self.visas),(self.passport_number)
    
    # def __init__(self,country,name,surname,birth_date,visas,passport_number):