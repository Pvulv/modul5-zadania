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

def generate_views():
    number_1 = fake.random_int(1,101)
    element = fake.random_int(0,len(Movies_Series) - 1)
    Movies_Series[element].Play = number_1

def auto_generate_views():
    for _ in range(10):
        generate_views()

def top_titles(content_type):

    top_title = ('', 0)
    name = ''
    for element in Movies_Series:
        if isinstance(element, content_type) == True and top_title[1] == 0:
            top_title = (element.title, element.num_views)
        elif isinstance(element, content_type) == True and element.num_views > top_title[1]:
            top_title = (element.title, element.num_views)
    return top_title

if __name__ == '__main__':

    print(' |  Biblioteka filmów  | ')

    Movies_Series.append(Movie(title='Piła', year='2004', category='Horror', num_views=0))
    Movies_Series.append(Series(title='Shadowhunters', year='2016', category='Dreszczowiec', num_views=0, num_season=[13, 20, 22]))
    Movies_Series.append(Movie(title='Koszmar z ulicy Wiązów', year='1984', category='Horror', num_views=0))
    Movies_Series.append(Series(title='Sherlock', year='2012', category='Kryminalny', num_views=0, num_season=[3, 3, 3, 3]))
    Movies_Series.append(Movie(title='Kruk. Zagadka zbrodni', year='2004', category='Dreszczowiec', num_views=0))
    Movies_Series.append(Movie(title='Jak stracić faceta w 10 dni', year='2003', category='Komedia', num_views=0))
    Movies_Series.append(Series(title='Euforia', year='2019', category='Dramat', num_views=0, num_season=[8, 8]))
    Movies_Series.append(Series(title='Hazbin Hotel', year='2024', category='Czarna komedia', num_views=0, num_season=[10]))
    Movies_Series.append(Movie(title='Ruchomy zamek Hauru', year='2004', category='Film familijny', num_views=0))
    Movies_Series.append(Series(title='Niania', year='2008', category='Komedia', num_views=0, num_season=[12, 10, 8, 10]))

    auto_generate_views()
    print(f'Najpopularniejsze filmy i seriale dnia {time}: \n Film: {top_titles(Movie)} \n Serial: {top_titles(Series)}')
    sorted_elements = sorted(Movies_Series, key= lambda element: element.num_views)
    print(' | Top 3 | ')
    print(sorted_elements[-1], ' | ', sorted_elements[-1].num_views)
    print(sorted_elements[-2], ' | ', sorted_elements[-2].num_views)
    print(sorted_elements[-3], ' | ', sorted_elements[-3].num_views)

    search()