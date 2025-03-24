from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from transactions.models import Transaction


class NewCreditTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('amount', 'wallet')


class NewDebitTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('amount', 'wallet')

    def validate(self, validated_data):
        wallet = validated_data['wallet']
        amount = validated_data['amount']

        if not wallet:
            raise ValidationError("wallet wasn't found")

        if not amount:
            raise ValidationError("you didn't specify the payment amount")

        balance = wallet.get_balance()
        if balance < amount:
            raise ValidationError("you haven't enough funds")

        validated_data['amount'] = amount * -1

        return validated_data


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('txid', 'amount', 'wallet')
