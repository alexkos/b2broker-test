from rest_framework import serializers

from wallets.models import Wallet


class CreateWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('label',)


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('label', 'balance')
