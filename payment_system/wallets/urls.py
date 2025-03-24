from django.urls import path

from wallets.views import CreateWalletView, WalletsView

app_name = 'wallets'


urlpatterns = [
    path('', WalletsView.as_view()),
    path('create', CreateWalletView.as_view()),
]
