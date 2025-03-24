import logging

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from wallets.filters import WalletFilter
from wallets.models import Wallet
from wallets.pagination import WalletPageNumberPagination
from wallets.serializers import CreateWalletSerializer, WalletSerializer

logger = logging.getLogger(__name__)


class WalletsView(ListModelMixin, GenericAPIView):
    queryset = Wallet.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = WalletSerializer
    pagination_class = WalletPageNumberPagination
    filterset_class = WalletFilter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['label', 'balance']

    def get(self, request, *args, **kwargs):
        logger.info('showing wallets')

        return self.list(request, *args, **kwargs)


class CreateWalletView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        logger.info('Creating wallet')

        serializer = CreateWalletSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response_serializer = CreateWalletSerializer(serializer.instance)

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
