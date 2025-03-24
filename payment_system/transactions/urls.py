from django.urls import path

from transactions.views import NewCreditTransactionView, NewDebitTransactionView, TransactionsView

app_name = 'transactions'


urlpatterns = [
    path('', TransactionsView.as_view()),
    path('credit/new', NewCreditTransactionView.as_view()),
    path('debit/new', NewDebitTransactionView.as_view()),
]
