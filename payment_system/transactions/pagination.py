from rest_framework.pagination import PageNumberPagination


class TransactionPageNumberPagination(PageNumberPagination):
    default_limit = 2
