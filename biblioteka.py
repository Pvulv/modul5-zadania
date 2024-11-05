from faker import Faker
fake = Faker()

from datetime import date
time = date.today()

Movies_Series = []

class BaseInfo:
    def __init__(self, title, year, category, num_views = 0):
        self.title = title
        self.year = year
        self.category = category
        self.num_views = num_views

    @property
    def Play(self):
        self.num_views += 1
        return self.num_views
    
    @Play.setter
    def Play(self, value):
        self.num_views += value
    
    def __str__(self):
        return f"{self.title} ({self.year})"
