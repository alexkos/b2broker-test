from rest_framework.pagination import PageNumberPagination


class WalletPageNumberPagination(PageNumberPagination):
    default_limit = 5
