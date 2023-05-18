import requests

def get_token_data(client_name, client_email):
    url = 'https://simple-books-api.glitch.me/api-clients/'
    json_data = {
        'clientName': client_name,
        'clientEmail': client_email
    }
    response = requests.post(url=url, json=json_data)
    return response