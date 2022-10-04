from rest_framework import serializers
from walletapp.models import Customer, Wallet, Account, Card, Transaction, Loan, Receipt, Notification

class CustomerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'age', 'address',)

class WalletSerializer(serializers.ModelSerializer):        
     class Meta:
         model =  Wallet
         fields = "__all__"  
         
class AccountSerializer(serializers.ModelSerializer):        
     class Meta:
         model =  Account
         fields = "__all__" 
         
class CardSerializer(serializers.ModelSerializer):        
     class Meta:
         model =  Card
         fields = "__all__"          
         
class LoanSerializer(serializers.ModelSerializer):        
     class Meta:
         model =  Loan 
         fields = "__all__" 
         
class TransactionSerializer(serializers.ModelSerializer):        
     class Meta:
         model =  Transaction
         fields = "__all__" 
         
class ReceiptSerializer(serializers.ModelSerializer):        
     class Meta:
         model =  Receipt
         fields = "__all__" 
         
class NotificationSerializer(serializers.ModelSerializer):        
     class Meta:
         model =  Notification
         fields = "__all__"                                   