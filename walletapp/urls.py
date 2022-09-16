from django.urls import path
from .views import list_accounts, list_customers, register_account, register_card, register_currency, register_customer, register_loan, register_notifications, register_receipt, register_reward, register_thirdparty, register_transaction,register_wallet


urlpatterns = [
    path('customer/', register_customer, name="customer"),
    path('wallet/', register_wallet, name="wallet"),
    path('account/', register_account, name="account"),
    path('card/', register_card, name="card"),
    path('currency/', register_currency, name="currency"),
    path('loan/', register_loan, name="loan"),  
    path('notifications/', register_notifications, name="notifications"),
    path('receipt/', register_receipt, name="receipt"),
    path('reward/', register_reward, name="reward"),
    path('thirdparty/', register_thirdparty, name="thirdparty"),
    path('transaction/', register_transaction, name="transaction"),
    path('customers/', list_customers, name="customers_list"),
    path('accounts/', list_accounts, name="accounts_list"),
]
