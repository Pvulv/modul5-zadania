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