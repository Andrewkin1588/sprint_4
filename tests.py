import pytest

from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize('book, length', [
        ['Война и Мир', 1],
        ['ПушкинПушкинПушкинПушкинПушкинПушкинПушкин', 0],
        ['', 0]
    ]
                             )
    def test_add_new_book_add_one_book(self, book, length):
        collector = BooksCollector()

        collector.add_new_book(book)
        assert len(collector.get_books_genre()) == length

    def test_add_new_book_add_two_similar(self):
        collector = BooksCollector()

        collector.add_new_book('Война и Мир')
        collector.add_new_book('Война и Мир')

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('added_book, seted_book, genre, expected', [
        ['Война и Мир', 'Война и Мир', 'Фантастика', 'Фантастика'],
        ['Война и Мир', 'Война и Мир', 'Триллер', ''],
        ['Война и Мир', 'Кладбище домашних животных', 'Фантастика', None]
    ])
    def test_set_book_genre_book_in_books_genre(self, added_book, seted_book, genre, expected):
        collector = BooksCollector()

        collector.add_new_book(added_book)
        collector.set_book_genre(seted_book, genre)

        assert collector.get_book_genre(seted_book) == expected

    @pytest.mark.parametrize('added_book, genre, expected', [
        ['Война и Мир', 'Фантастика', ['Война и Мир']],
        ['Война и Мир', 'Триллер', []],
        ['', 'Фантастика', []]
    ])
    def test_get_books_with_specific_genre_add_and_get_specific_genre(self, added_book, genre, expected):
        collector = BooksCollector()

        collector.add_new_book(added_book)
        collector.set_book_genre(added_book, genre)

        assert collector.get_books_with_specific_genre(genre) == expected

    @pytest.mark.parametrize('added_book, genre, expected', [
        ['Война и Мир', 'Фантастика', ['Война и Мир']],
        ['Война и Мир', 'Триллер', []],
        ['Война и Мир', 'Ужасы', []]
    ])
    def test_get_books_for_children_genre_add_and_get_children_genre(self, added_book, genre, expected):
        collector = BooksCollector()

        collector.add_new_book(added_book)
        collector.set_book_genre(added_book, genre)

        assert collector.get_books_for_children() == expected

    def test_add_book_in_favorites_add_books_positive(self):
        collector = BooksCollector()

        collector.add_new_book('Война и Мир')
        collector.add_book_in_favorites('Война и Мир')
        assert collector.get_list_of_favorites_books() == ['Война и Мир']

    def test_delete_book_from_favorites_delete_book_positive(self):
        collector = BooksCollector()

        collector.add_new_book('Война и Мир')
        collector.add_book_in_favorites('Война и Мир')
        collector.delete_book_from_favorites('Война и Мир')

        assert collector.get_list_of_favorites_books() == []
