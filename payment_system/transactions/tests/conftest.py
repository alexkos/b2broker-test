import pytest

from transactions.models import Transaction
from wallets.tests.conftest import wallet


@pytest.fixture
def credit_transaction(wallet):
    transaction = Transaction.objects.create(amount=100, wallet=wallet)

    return transaction


@pytest.fixture
def debit_transaction(wallet):
    transaction = Transaction.objects.create(amount=-10, wallet=wallet)

    return transaction
