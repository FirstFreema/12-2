class Film:
    def __init__(self, title, genre, director, year, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def get_info(self):
        actor_info = "\n".join([f"{actor['name']} - {actor['role']}" for actor in self.actors])
        return f"""
        Название: {self.title}
        Жанр: {self.genre}
        Режиссер: {self.director}
        Год выпуска: {self.year}
        Длительность: {self.duration} минут
        Студия: {self.studio}
        Актеры:
        {actor_info}
        """

class FilmController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def display_film_info(self):
        film_info = self.model.get_info()
        self.view.display(film_info=film_info)

    def create_film(self, title, genre, director, year, duration, studio, actors):
        film = self.model(title, genre, director, year, duration, studio, actors)
        return film

class FilmView:
    def display(self, film_info):
        print(film_info)


# Пример
actors = [
    {'name': 'Том Хэнкс', 'role': 'Главная роль'},
    {'name': 'Мэрил Стрип', 'role': 'Второстепенная роль'}
]
film = FilmController(Film, FilmView).create_film(
    'Форрест Гамп', 'Драма', 'Роберт Земекис', 1994, 142, 'Paramount Pictures', actors
)
FilmController(film, FilmView).display_film_info()
