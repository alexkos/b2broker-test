import uuid

from django.db import models, transaction

from wallets.models import Wallet


class Transaction(models.Model):
    txid = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=36, decimal_places=18)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transactions')

    def __str__(self):
        return f'{self.txid}({self.wallet.label})'

    def __repr__(self):
        return f'{self.txid}({self.wallet.label})'

    def save(self, *args, **kwargs):
        with transaction.atomic():
            wallet = Wallet.objects.select_for_update().get(id=self.wallet_id)

            self.txid = f'{uuid.uuid4()}'
            super().save(*args, **kwargs)
            wallet.update_balance()
