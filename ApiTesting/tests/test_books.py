from request_folder.books import get_all_books
from request_folder.books import get_book_by_id

class TestAllBooks:

    def test_with_no_filters(self):
        response = get_all_books()
        assert response.status_code == 200
        assert len(response.json()) == 6

    def test_with_type_fiction(self):
        r1 = get_all_books('fiction')
        assert r1.status_code == 200
        assert len(r1.json()) == 4

    def test_with_type_non_fiction(self):
        r2 = get_all_books('non-fiction')
        assert r2.status_code == 200
        assert len(r2.json()) == 2

    def test_with_type_not_accepted(self):
        r3 = get_all_books('romance')
        assert r3.status_code == 400
        r3_data = r3.json()
        expected = "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction."
        actual = r3_data.get("error", "Bad error!")
        assert expected == actual

    def test_with_type_not_valid(self):
        r4 = get_all_books('123')
        r4_data = r4.json()
        expected = "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction."
        actual = r4_data.get("error", "Another error")
        assert r4.status_code == 400
        assert actual == expected

    def test_with_limit_accepted(self):
        r5 = get_all_books(None, 4)
        assert r5.status_code == 200
        assert len(r5.json()) == 4

    def test_with_lowest_limit_1(self):
        r6 = get_all_books(None, 1)
        assert r6.status_code == 200
        assert len(r6.json()) == 1

    def test_with_highest_limit_20(self):
        r7 = get_all_books(None, 20)
        assert r7.status_code == 200
        assert len(r7.json()) == 6

    def test_with_negative_limit(self):
        r8_negative = get_all_books(None, -1)
        assert r8_negative.status_code == 400
        assert r8_negative.json().get('error',
                                      'Bad error') == "Invalid value for query parameter 'limit'. Must be greater than 0."

    def test_with_higher_limit(self):
        r9 = get_all_books(None, 21)
        assert r9.status_code == 400
        assert r9.json().get('error',
                                     'Bad error') == "Invalid value for query parameter 'limit'. Cannot be greater than 20."

    def test_with_limit_0(self):
        r10 = get_all_books(None, 0)
        assert r10.status_code == 200
        assert len(r10.json()) == 6

    def test_with_limit_special_character(self):
        r11 = get_all_books(None, 0)
        assert r11.status_code == 200
        assert len(r11.json()) == 6

    def test_with_limit_0_and_type_fiction(self):  # Negative testing
        r12 = get_all_books('fiction', 0)
        assert r12.status_code == 200
        assert len(r12.json()) == 4

    def test_with_limit_string_and_type_fiction(self):  # Negative testing
        r13 = get_all_books('fiction', 'limit')
        assert r13.status_code == 200
        assert len(r13.json()) == 4

    def test_with_limit_21_and_type_fiction(self):
        r14 = get_all_books('fiction', 21)
        assert r14.status_code == 400
        assert r14.json().get('error',
                                      'Bad error') == "Invalid value for query parameter 'limit'. Cannot be greater than 20."

class TestBookByID:

    def test_with_id_valid_and_book_in_database(self):
        r15 = get_book_by_id(1)
        assert r15.status_code == 200
        assert len(r15.json()) == 8

    def test_with_id_valid_and_book_not_in_database(self):
        r16 = get_book_by_id(7)
        assert r16.status_code == 404
        assert r16.json().get('error', 'Bad error') == "No book with id 7"

    def test_with_id_0(self):
        r16 = get_book_by_id(0)
        assert r16.status_code == 404
        assert r16.json().get('error', 'Bad error') == "No book with id 0"

    def test_with_id_higher_than_limit(self):
        r17 = get_book_by_id(21)
        assert r17.status_code == 404
        assert r17.json().get('error', 'Bad error') == "No book with id 21"

    def test_with_id_special_char(self):
        r17 = get_book_by_id('@')
        assert r17.status_code == 404
        assert r17.json().get('error', 'Bad error') == "No book with id NaN"



