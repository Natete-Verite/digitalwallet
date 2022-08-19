from django.contrib import admin
# Register your models here.
from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet, Currency

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'email')
    search_fields = ('first_name', 'last_name')
admin. site.register(Customer,CustomerAdmin)
    
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_name', 'account_number', 'account_type')
    search_fields = ('account_name', 'account_number','account_type')
admin.site.register(Account,AccountAdmin)    
    
class WalletAdmin(admin.ModelAdmin): 
    list_display = ('customer', 'status', 'amount')
    search_fields = ('customer', 'status', 'amount')
admin.site.register(Wallet,WalletAdmin)
    
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_type', 'transaction_description', 'message')
    search_fields = ('transaction_type', 'transaction_description', 'message')
admin.site.register(Transaction,TransactionAdmin)    
    
class CardAdmin(admin.ModelAdmin):   
    list_display = ('wallet', 'account', 'issuer')
    search_fields = ('wallet', 'account', 'issuer')
admin.site.register(Card,CardAdmin)    
    
class ThirdPartyAdmin(admin.ModelAdmin): 
    list_display = ('wallet', 'issuer', 'account')
    search_fields = ('wallet', 'issuer', 'account')
admin.site.register(ThirdParty,ThirdPartyAdmin)    
    
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'date', 'title')
    search_fields = ('recipient', 'date', 'title')
admin.site.register(Notification,NotificationAdmin)    
    
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount', 'transaction')
    search_fields = ('date', 'amount', 'transaction')
admin.site.register(Receipt,ReceiptAdmin)   
    
class LoanAdmin(admin.ModelAdmin):
    list_display = ('wallet', 'guaranter', 'issuer')
    search_fields = ('wallet', 'guaranter', 'issuer')
admin.site.register(Loan,LoanAdmin)    
    
class RewardAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'recipient', 'points')
    search_fields = ('transaction', 'recipient', 'points')
admin.site.register(Reward,RewardAdmin)    
    
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('country', 'symbol', 'amount')
    search_fields = ('country', 'symbol', 'amount')
admin.site.register(Currency,CurrencyAdmin)    