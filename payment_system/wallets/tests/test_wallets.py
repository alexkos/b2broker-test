import pytest

from wallets.models import Wallet

pytestmark = pytest.mark.django_db

HTTP_STATUS_OK = 200
HTTP_STATUS_CREATED = 201
BAD_REQUEST = 400


def test_create_wallet(client):
    data = {'label': 'My Wallet'}

    response = client.post('/wallets/create', data, format='json')

    assert response.status_code == HTTP_STATUS_CREATED
    assert Wallet.objects.count() == 1

    wallet = Wallet.objects.first()
    assert wallet.label == 'My Wallet'


def test_create_wallet_without_label(client):
    response = client.post('/wallets/create', {}, format='json')
    assert response.status_code == BAD_REQUEST


def test_show_wallets(client, wallet):
    response = client.get('/wallets/')

    assert response.status_code == HTTP_STATUS_OK
    assert len(response.data['results']) > 0

    result = response.data['results'][0]
    assert result['label'] == 'no_balance'
