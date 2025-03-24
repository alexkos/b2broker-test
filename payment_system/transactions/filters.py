from django_filters import FilterSet, NumberFilter

from transactions.models import Transaction


class TransactionFilter(FilterSet):
    min_amount = NumberFilter(field_name='amount', lookup_expr='gte')
    max_amount = NumberFilter(field_name='amount', lookup_expr='lte')
    wallet = NumberFilter(field_name='wallet_id')

    class Meta:
        model = Transaction
        fields = ['min_amount', 'max_amount', 'wallet']
