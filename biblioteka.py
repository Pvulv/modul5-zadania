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

class Movie(BaseInfo):
    def __init__(self, title, year, category, num_views = 0):
        super().__init__(title, year, category, num_views)

class Series(BaseInfo):
    def __init__(self, title, year, category, num_views = 0, num_season = []):
        super().__init__(title, year, category, num_views)
        self.num_season = num_season
    
    def display_episodes(self):
        episode_list = [f"S{season_num:02}E{episode_num:02}"
                        for season_num, num_ep in enumerate(self.num_season, start=1)
                        for episode_num in range(1, num_ep + 1)]
        return "\n".join(episode_list)
    
    def __str__(self):
        return f"{self.title}"

def getMovie():
    print(' | Filmy | ')
    for movie in Movies_Series:
        if isinstance(movie,Movie) == True:
            print(movie)

def getSeries():
    print(' | Seriale | ')
    for serie in Movies_Series:
        if isinstance(serie,Series) == True:
            print(serie)
