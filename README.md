# qa_python
test_add_new_book_invalid_name_too_long проверяет корректность обработки ситуации, 
когда пользователь пытается добавить новую книгу с именем, длина которого превышает максимально допустимое значение.

test_add_new_book_invalid_name_empty_string проверяет поведение метода add_new_book в случае попытки добавить книгу 
с пустым именем.

test_set_book_genre_valid_inputs проверяет правильное функционирование метода set_book_genre 
при передаче валидных значений.

test_get_book_genre_invalid_input_book_not_found проверяет поведение метода get_book_genre в случае, 
когда запрашивается информация о книге, которая отсутствует в коллекции.

test_get_books_with_specific_genre_valid_input проверяет корректную работу метода get_books_with_specific_genre 
при запросе списка книг определенного жанра.

test_get_books_genre_valid_input проверяет корректность работы метода get_books_genre при получении словаря 
с информацией о книгах и их жанрах.

test_get_books_for_children_valid_input_exclude_adult_genres проверяет работу метода get_books_for_children, 
который должен возвращать список книг, подходящих для детей, исключая те, которые относятся к взрослым жанрам.

test_get_books_for_children_invalid_input_include_adult_genre проверяет работу метода get_books_for_children 
в том случае, когда в коллекции присутствуют книги взрослых жанров, которые не предназначены для детей.

test_add_book_in_favorites_valid_input проверяет работу метода add_book_in_favorites при добавлении в избранное книги, 
которая уже существует в коллекции.

test_delete_book_from_favorites_valid_input проверяет работу метода delete_book_from_favorites 
при удалении книги из избранного, если она содержится в списке избранных книг.



















