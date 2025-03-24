from django.db import models
from django.db.models import Sum


class Wallet(models.Model):
    label = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=36, decimal_places=18, default=0)

    def __str__(self):
        return self.label

    def __repr__(self):
        return self.label

    def get_balance(self):
        return self.transactions.aggregate(balance=Sum('amount'))['balance'] or 0

    def update_balance(self):
        self.balance = self.get_balance()
        self.save()
