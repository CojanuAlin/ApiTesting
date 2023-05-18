from request_folder.orders import submit_order
from request_folder.orders import get_book_orders


class TestSubmitOrder:

    token = '3a97b641e70c389f30e415bd764c92c9354f11fdae84332dd9d57623582cd273'

    def test_sumbit_order_with_all_data_valid(self):
        response = submit_order(1, 'Alin', self.token)
        assert response.status_code == 201
        assert len(response.json()) == 2

    def test_sumbit_order_with_wrong_token(self):
        response = submit_order(1, 'Alin', '1234123')
        assert response.status_code == 401
        assert response.json().get('error', 'No error') == "Invalid bearer token."

    def test_sumbit_order_with_id_in_limit_and_book_not_in_stock(self):
        response = submit_order(7, 'Alin', self.token)
        assert response.status_code == 400
        assert response.json().get('error', 'No error') == "Invalid or missing bookId."

    def test_sumbit_order_with_id_special_char(self):
        response = submit_order("@#", 'Alin', self.token)
        assert response.status_code == 400
        assert response.json().get('error', 'No error') == "Invalid or missing bookId."

    def test_sumbit_order_with_id_letter(self):
        response = submit_order("a", 'Alin', self.token)
        assert response.status_code == 400
        assert response.json().get('error', 'No error') == "Invalid or missing bookId."

    def test_sumbit_order_with_no_customer_name(self):
        response = submit_order(2, " ", self.token)
        assert response.status_code == 404
        assert response.json().get('error', 'No error') == "This book is not in stock. Try again later."

    def test_sumbit_order_with_id_4(self):
        response = submit_order(4, 'Alin', self.token)
        print(response.json())
        assert response.status_code == 201
        assert len(response.json()) == 2

    def test_get_orders(self):
        response = get_book_orders('Yw3D_kfyi6Xy0oVJxBsaR')
        assert response.status_code == 200
        assert len(response.json()) == 6
