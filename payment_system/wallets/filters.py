from django_filters import FilterSet, NumberFilter

from wallets.models import Wallet


class WalletFilter(FilterSet):
    min_balance = NumberFilter(field_name='balance', lookup_expr='gte')
    max_balance = NumberFilter(field_name='balance', lookup_expr='lte')
    label = NumberFilter(field_name='label', lookup_expr='icontains')

    class Meta:
        model = Wallet
        fields = ['min_balance', 'max_balance', 'label']
