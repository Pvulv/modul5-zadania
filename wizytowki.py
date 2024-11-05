from faker import Faker
fake = Faker()

class BusinessCards:
    def __init__(self, name, last_name, company, job, email):
        self.name = name
        self.last_name = last_name
        self.company = company
        self.job = job
        self.email = email
        self._number_letters = 0
    @property
    def number_letters(self):
        return f"  {self.name} {self.last_name} ma {len(self.name)} i {len(self.last_name)} liter w imieniu i nazwisku czyli łącznie {self._number_letters}"
    @number_letters.setter
    def number_letters(self, value):
        self._number_letters = value
        return self._number_letters

class BaseContact(BusinessCards):
    def __init__(self, priv_number, name, last_name, email):
        super().__init__(name, last_name, None, None, email)
        self.priv_number = priv_number
    def contact(self):
        print(f" Wybieram numer {self.priv_number} i dzwonię do {self.name} {self.last_name}")
    def __str__(self):
        return f"{self.name}, {self.last_name}, {self.email}, {self.priv_number}"

class BusinessContact(BusinessCards):
    def __init__(self, name, last_name, company, job, business_number):
        super().__init__(name, last_name, company, job, None)
        self.business_number = business_number
    def contact(self):
        print(f" Wybieram numer {self.business_number} i dzwonię do {self.name} {self.last_name}")
    def __str__(self):
        return f"{self.company}, {self.job}, {self.business_number}"

BasePeople = []
BusinessPeople = []

def create_contacts():
    for i in range(fake.random_int(1,5)):
        BasePeople.append(BaseContact(priv_number=fake.phone_number(), name=fake.name(), last_name=fake.last_name(), email=fake.email()))    
    
    for z in range(fake.random_int(1,7)):
        BusinessPeople.append(BusinessContact(name=fake.name(), last_name=fake.last_name(), company=fake.company(), business_number=fake.phone_number(), job=fake.job()))

create_contacts()