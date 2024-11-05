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

def search():
    search_again = True
    while search_again:
        question_1 = input("Chcesz zobaczyć listę wszystkich filmów czy seriali? (Wpisz 'M' dla filmów lub 'S' dla seriali): ").strip().upper()
        
        if question_1 == 'M':
            getMovie()
            question_2 = input('Wybierz, który film chcesz obejrzeć (Napisz dokładny tytuł): ').strip()
            found = False
            for item in Movies_Series:
                if isinstance(item, Movie) and item.title.lower() == question_2.lower():
                    item.Play
                    print(f"Obejrzano film: {item.title}. Liczba wyświetleń: {item.num_views}")
                    found = True
                    break
            if not found:
                print("Nie znaleziono filmu o podanym tytule.")
                
        elif question_1 == 'S':
            getSeries()
            question_2 = input('Wybierz, który serial chcesz obejrzeć (Napisz dokładny tytuł): ').strip()
            found = False
            for item in Movies_Series:
                if isinstance(item, Series) and item.title.lower() == question_2.lower():
                    print(f"\nWybrano serial: {item.title}")
                    print("Lista dostępnych odcinków:")
                    print(item.display_episodes())
                    episode_choice = input("Wybierz numer sezonu i odcinka w formacie S01E01: ").strip().upper()
                    
                    episode_found = False
                    for season_num, num_ep in enumerate(item.num_season, start=1):
                        for episode_num in range(1, num_ep + 1):
                            episode_id = f"S{season_num:02}E{episode_num:02}"
                            if episode_id == episode_choice:
                                print(f"Obejrzano {episode_id} z serialu {item.title}")
                                item.Play
                                episode_found = True
                                break
                        if episode_found:
                            break
                    if not episode_found:
                        print("Nie znaleziono takiego odcinka.")
                    found = True
                    break
            if not found:
                print("Nie znaleziono serialu o podanym tytule.")
        else:
            print("Podano złą wartość, spróbuj ponownie!")
        
        search_again = input('Czy chcesz kontynuować (T lub N): ').strip().upper()
        if search_again == 'N':
            search_again = False
