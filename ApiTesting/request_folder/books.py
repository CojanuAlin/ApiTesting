import requests

def get_all_books(type=None, limit=None):
    url = 'https://simple-books-api.glitch.me/books'
    if bool(type) and bool(limit):
        url += f'?type={type}&limit={limit}'
    elif bool(type):
        url += f'?type={type}'
    elif bool(limit):
        url += f'?limit={limit}'
    response = requests.get(url=url)
    print(response.json())
    print(response.status_code)
    return response

get_all_books()
get_all_books('fiction', 2)
get_all_books('non-fiction')
get_all_books(None, 4)

