class Article:
    def __init__(self, title, author, char_count, publication, description):
        self.title = title
        self.author = author
        self.char_count = char_count
        self.publication = publication
        self.description = description

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_char_count(self):
        return self.char_count

    def get_publication(self):
        return self.publication

    def get_description(self):
        return self.description

    def set_title(self, new_title):
        self.title = new_title

    def set_author(self, new_author):
        self.author = new_author

    def set_char_count(self, new_char_count):
        self.char_count = new_char_count

    def set_publication(self, new_publication):
        self.publication = new_publication

    def set_description(self, new_description):
        self.description = new_description


class ArticleModel:
    def __init__(self):
        self.articles = []

    def add_article(self, article):
        self.articles.append(article)

    def get_articles(self):
        return self.articles


class ArticleController:
    def __init__(self, model):
        self.model = model

    def create_article(self, title, author, char_count, publication, description):
        article = Article(title, author, char_count, publication, description)
        self.model.add_article(article)

    def get_articles(self):
        return self.model.get_articles()

class ArticleView:
    def display_articles(self, articles):
        for article in articles:
            print(f"Название: {article.get_title()}")
            print(f"Автор: {article.get_author()}")
            print(f"Количество символов: {article.get_char_count()}")
            print(f"Публикация: {article.get_publication()}")
            print(f"Краткое описание: {article.get_description()}")
            print()


# Проверка
article_model = ArticleModel()
article_controller = ArticleController(article_model)
article_controller.create_article(
    "Обзор библиотек обучения нейронных сетей на языке Python",
    "Балбанов Никита Романович",
    2500,
    "Молодой ученый №46 (336) ноябрь 2020",
    "Обзор самых популярных библиотек маштнного языка Python."
)

article_controller.create_article(
    "Язак программирования Python. Библиотеки Python",
    "Таршхоева Жанетта Тархановна",
    3800,
    "Молодой ученый №5 (347) январь 2021",
    "Машинное обучение и анализ данных на Python."
)

article_view = ArticleView()
articles = article_controller.get_articles()
article_view.display_articles(articles)
