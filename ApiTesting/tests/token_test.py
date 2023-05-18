from request_folder.token_auth import get_token_data


class TestGetToken:
    def test_get_toke_with_registred_user(self):
        pass

    def test_get_token_with_not_registred_user(self):
        response = get_token_data('Alin', 'alin@user.com')
        assert response.status_code == 201
        assert bool(response.json().get('accessToken', False)) is True
