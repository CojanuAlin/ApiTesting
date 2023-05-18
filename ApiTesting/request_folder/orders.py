import requests


def submit_order(book_id, customer_name, token):

    json_data = {
        "bookId": book_id,
        "customerName": customer_name
    }

    headers_data = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.post(
        url='https://simple-books-api.glitch.me/orders',
        json=json_data,
        headers=headers_data
    )

    return response

def get_book_orders(book_id):
    url = f'https://simple-books-api.glitch.me/orders/{book_id}'
    response = requests.get(url=url)
    return response

