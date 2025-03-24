import pytest

from transactions.models import Transaction
from wallets.tests.conftest import wallet, wallet_with_balance

pytestmark = pytest.mark.django_db

HTTP_STATUS_OK = 200
HTTP_STATUS_CREATED = 201


def test_create_credit_transaction(client, wallet):
    data = {
        'amount': 100,
        'wallet': wallet.id,
    }

    response = client.post('/transactions/credit/new', data, format='json')
    assert response.status_code == HTTP_STATUS_CREATED
    assert Transaction.objects.count() == 1


def test_create_debit_transaction_negative_balance(client, wallet):
    data = {
        'amount': 100,
        'wallet': wallet.id,
    }

    for number_tx in range(3):
        client.post('/transactions/credit/new', data, format='json')

    response = client.post('/transactions/debit/new', data, format='json')
    assert response.status_code == HTTP_STATUS_CREATED
    assert Transaction.objects.count() == 4


def test_show_transactions(client, credit_transaction, debit_transaction):
    response = client.get('/transactions/')
    assert response.status_code == HTTP_STATUS_OK
    assert len(response.data['results']) > 0


def test_filter_transactions_by_amount(client, wallet_with_balance):
    response = client.get('/transactions/?amount_lte=100')
    assert response.status_code == HTTP_STATUS_OK
    assert all(float(tx['amount']) <= 100 for tx in response.data['results'])
