import logging
import random

from django.core.management import BaseCommand

from transactions.models import Transaction
from wallets.models import Wallet

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        logger.info('start generate data')

        for number in range(1, 10):
            Wallet.objects.create(label=f'wallet_{number}')

        wallets = Wallet.objects.all()

        for wallet in wallets:
            for number in range(1, 6):
                value = random.randrange(-20, 100)
                Transaction.objects.create(amount=value, wallet=wallet)

        logger.info('finish generate data')
