import pytest

from transactions.models import Transaction, Wallet


@pytest.fixture
def wallet():
    return Wallet.objects.create(label='no_balance')


@pytest.fixture
def wallet_with_balance():
    wallet = Wallet.objects.create(label='with_balance')
    Transaction.objects.create(wallet=wallet, amount=100, txid='74935bb7-94a4-41af-9084-875a2ef4ec7c')
    return wallet
