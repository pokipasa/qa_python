import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    @pytest.mark.parametrize(
        "book_title",
        [
            ("Вторая жизнь Уве"),
            ("Это очень очень очень очень длинное имя книги")
        ]
    )
    def test_add_new_book_invalid_name_too_long(self, book_title):
        collector = BooksCollector()
        collector.add_new_book(book_title)
        if len(book_title) > 41:
            assert book_title not in collector.get_books_genre()
        else:
            assert book_title in collector.get_books_genre()

    def test_add_new_book_invalid_name_empty_string(self):
        collector = BooksCollector()
        collector.add_new_book("")
        assert "" not in collector.get_books_genre()

    def test_set_book_genre_valid_inputs(self):
        collector = BooksCollector()
        collector.add_new_book("Вторая Жизнь Уве")
        assert collector.get_book_genre("Вторая Жизнь Уве") == ''
        collector.set_book_genre("Вторая Жизнь Уве", "Комедии")
        assert collector.get_book_genre("Вторая Жизнь Уве") == "Комедии"

    def test_get_book_genre_invalid_input_book_not_found(self):
        collector = BooksCollector()
        assert collector.get_book_genre("Рука в мясорубке") is None

    def test_get_books_with_specific_genre_valid_input(self):
        collector = BooksCollector()
        collector.add_new_book("Рука в мясорубке")
        collector.add_new_book("Настоящий детектив")
        collector.add_new_book("Совмещение учёбы и работы")
        collector.set_book_genre("Рука в мясорубке", "Ужасы")
        collector.set_book_genre("Настоящий детектив", "Детективы")
        collector.set_book_genre("Совмещение учёбы и работы", "Ужасы")
        horror_books = collector.get_books_with_specific_genre("Ужасы")
        assert len(horror_books) == 2
        assert all(book in horror_books for book in ["Рука в мясорубке", "Совмещение учёбы и работы"])

    def test_get_books_genre_valid_input(self):
        collector = BooksCollector()
        collector.add_new_book("Совмещение учёбы и работы")
        collector.add_new_book("Настоящий детектив")
        collector.set_book_genre("Совмещение учёбы и работы", "Ужасы")
        collector.set_book_genre("Настоящий детектив", "Детективы")
        books_genre = collector.get_books_genre()
        assert len(books_genre) == 2
        assert books_genre["Совмещение учёбы и работы"] == "Ужасы"
        assert books_genre["Настоящий детектив"] == "Детективы"

    def test_get_books_for_children_valid_input_exclude_adult_genres(self):
        collector = BooksCollector()
        collector.add_new_book("Время приключений")
        collector.set_book_genre("Время приключений", "Мультфильмы")
        children_books = collector.get_books_for_children()
        assert "Время приключений" in children_books

    def test_get_books_for_children_invalid_input_include_adult_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Совмещение учёбы и работы")
        collector.set_book_genre("Совмещение учёбы и работы", "Ужасы")
        children_books = collector.get_books_for_children()
        assert "Совмещение учёбы и работы" not in children_books

    def test_add_book_in_favorites_valid_input(self):
        collector = BooksCollector()
        collector.add_new_book("Вторая жизнь Уве")
        collector.add_book_in_favorites("Вторая жизнь Уве")
        favorites = collector.get_list_of_favorites_books()
        assert "Вторая жизнь Уве" in favorites

    def test_delete_book_from_favorites_valid_input(self):
        collector = BooksCollector()
        collector.add_new_book("Вторая жизнь Уве")
        collector.add_book_in_favorites("Вторая жизнь Уве")
        collector.delete_book_from_favorites("Вторая жизнь Уве")
        favorites = collector.get_list_of_favorites_books()
        assert "Вторая жизнь Уве" not in favorites
