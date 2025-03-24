import logging

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from transactions.filters import TransactionFilter
from transactions.models import Transaction
from transactions.pagination import TransactionPageNumberPagination
from transactions.serializers import (
    NewCreditTransactionSerializer,
    NewDebitTransactionSerializer,
    TransactionSerializer,
)

logger = logging.getLogger(__name__)


class TransactionsView(ListModelMixin, GenericAPIView):
    queryset = Transaction.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = TransactionSerializer
    pagination_class = TransactionPageNumberPagination
    filterset_class = TransactionFilter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['amount', 'wallet']

    def get(self, request, *args, **kwargs):
        logger.info('showing transactions')

        return self.list(request, *args, **kwargs)


class NewCreditTransactionView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        logger.info('processing credit transaction')

        serializer = NewCreditTransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response_serializer = TransactionSerializer(serializer.instance)

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


class NewDebitTransactionView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        logger.info('processing debit transaction')

        serializer = NewDebitTransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response_serializer = TransactionSerializer(serializer.instance)

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
