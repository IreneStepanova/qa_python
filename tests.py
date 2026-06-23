import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
#Книга не добавляется, если наименование содержит пустое значение, 41 символ и больше 40 символа
    @pytest.mark.parametrize("invalid_name", [
            "",  # пустое название
            "А" * 41,  # 41 символ
            "Очень длинное название книги, которое точно должно превышать сорок символов",
        ])
    def test_add_new_book_invalid_names(self, invalid_name):
        collector = BooksCollector()
        initial_length = len(collector.get_books_genre())
        collector.add_new_book(invalid_name)
        assert len(collector.get_books_genre()) == initial_length
        assert invalid_name not in collector.get_books_genre()
#Книга не добавляется повторно
    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book("Дюна")
        collector.add_new_book("Дюна")
        assert len(collector.get_books_genre()) == 1
        assert collector.get_books_genre()["Дюна"] == ""

# ====== тесты для проверки класса по устанавке книге жанра=====
#Установка жанра для существующей книги
    def test_set_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book("Автостопом по Галактике")
        collector.set_book_genre("Автостопом по Галактике", "Фантастика")
        assert collector.get_book_genre("Автостопом по Галактике") == "Фантастика"
# =======Тест для проверки получения жанра книги по её имени ====
# Получение жанра сущесвтвующей книги
    def test_get_book_genre_exists(self):
        collector = BooksCollector()
        collector.add_new_book("Автостопом по Галактике")
        collector.set_book_genre("Автостопом по Галактике", "Фантастика")
        assert collector.get_book_genre("Автостопом по Галактике") == "Фантастика"

# ===== Тест для проверки вывода списока книг с определённым жанром ====
# Получение списка книг с определенным жанром
    def test_get_books_with_specific_genre_should_return_only_matching_books(self):
        collector = BooksCollector()
        collector.add_new_book("Автостопом по Галактике")
        collector.add_new_book("Властелин колец")
        collector.set_book_genre("Автостопом по Галактике", "Фантастика")
        collector.set_book_genre("Властелин колец", "Фантастика")

        fantasy_books = collector.get_books_with_specific_genre("Фантастика")

        assert len(fantasy_books) == 2
        assert "Автостопом по Галактике" in fantasy_books
        assert "Властелин колец" in fantasy_books
# ===== Тест для проверки получения словаря books_genre ====
# Проверка, что метод возвращает словарь
    def test_get_books_genre_returns_dict(self):
        collector = BooksCollector()
        result = collector.get_books_genre()
        assert isinstance(result, dict)

# ===== Тест для проверки, что возвращаются книги, подходящие детям ======
# Искелючение книг без жанра из списка для детей
    def test_get_books_for_children_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        children_books = collector.get_books_for_children()
        assert len(children_books) == 0
        assert "Книга 1" not in children_books
        assert "Книга 2" not in children_books

# ===== Тест для проверки, что книгу можно добавить в Избранное
# Добавление книги в избранное
    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Автостопом по Галактике")
        collector.add_book_in_favorites("Автостопом по Галактике")
        assert "Автостопом по Галактике" in collector.get_list_of_favorites_books()

# ==== Тест для проверки, что книгу можно удалить из Избранного
# Удаление книги из избранного
    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Автостопом по Галактике")
        collector.add_book_in_favorites("Автостопом по Галактике")
        collector.delete_book_from_favorites("Автостопом по Галактике")
        assert "Автостопом по Галактике" not in collector.get_list_of_favorites_books()

# ===== Тест для проверки получения списка Избранных книг
# Возвращение списка книг из Избранного
    def test_get_list_of_favorites_books_returns_list(self):
        collector = BooksCollector()
        result = collector.get_list_of_favorites_books()
        assert isinstance(result, list)