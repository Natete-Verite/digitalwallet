from django.shortcuts import render
from walletapp.models import Wallet
from .forms import AccountRegistrationForm, CardRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationRegistrationForm, ReceiptRegistrationForm, RewardRegistrationForm, ThirdPartyRegistrationForm, TransactionRegistrationForm
from .forms import WalletRegistrationForm
from .forms import CurrencyRegistrationForm
from . import models

# Create your views here.
def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomerRegistrationForm()    
    return render(request, "register_customer.html", {"form": form})
                                        
def register_wallet(request):
    if request.method == 'POST':
        form = WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = WalletRegistrationForm()    
    return render(request, "register_wallet.html", {"form": form})

def register_currency(request):
    if request.method == 'POST':
        form = CurrencyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CurrencyRegistrationForm()    
    return render(request, "register_currency.html", {"form": form}) 

def register_account(request):
    if request.method == 'POST':
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AccountRegistrationForm()    
    return render(request, "register_account.html", {"form": form}) 

def register_transaction(request):
    if request.method == 'POST':
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TransactionRegistrationForm()    
    return render(request, "register_transaction.html", {"form": form})

def register_card(request):
    if request.method == 'POST':
        form = CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CardRegistrationForm()    
    return render(request, "register_card.html", {"form": form}) 

def register_thirdparty(request):
    if request.method == 'POST':
        form = ThirdPartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ThirdPartyRegistrationForm()    
    return render(request, "register_thirdparty.html", {"form": form}) 

def register_notifications(request):
    if request.method == 'POST':
        form = NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NotificationRegistrationForm()    
    return render(request, "register_notification.html", {"form": form})

def register_receipt(request):
    if request.method == 'POST':
        form = ReceiptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReceiptRegistrationForm()    
    return render(request, "register_receipt.html", {"form": form}) 

def register_loan(request):
    if request.method == 'POST':
        form = LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LoanRegistrationForm()    
    return render(request, "register_loan.html", {"form": form})

def register_reward(request):
    if request.method == 'POST':
        form = RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RewardRegistrationForm()    
    return render(request, "register_reward.html", {"form": form})
                            
def list_customers(request):
    customers = models.Customer.objects.all()   
    return render(request, "customers_list.html", {"customers":customers})   

def list_accounts(request):
    accounts = models.Account.objects.all()
    return render(request, "accounts_list.html",{'accounts': accounts})

def list_wallets(request):
    wallets = models.Wallet.objects.all()
    return render(request, "wallets_list.html", {'wallets': wallets})

def list_transactions(request):
    transactions = models.Transaction.objects.all()
    return render(request, "transactions_list.html",{'transactions': transactions})

def list_currencies(request):
    currencies = models.Currency.objects.all()
    return render(request, 'currencies_list.html',{'currencies': currencies})

def list_receipts(request):
    receipts = models.Receipt.objects.all()
    return render(request, "receipts_list.html",{'receipts': receipts})

def list_cards(request):
    cards = models.Card.objects.all()
    return render(request, "cards_list.html",{'cards': cards})

def list_loans(request):
    loans = models.Loan.objects.all()
    return render(request, "loans_list.html",{'loans': loans})

def list_rewards(request):
    rewards = models.Reward.objects.all()
    return render(request, "rewards_list.html", {'rewards': rewards})

def list_thirdparties(request):
    thirdparties = models.ThirdParty.objects.all()
    return render(request, "thirdparties_list.html",{'thirdparties': thirdparties})

def list_notifications(request):
    notifications = models.Notification.objects.all()
    return render(request, 'notifications_list.html',
    {'notifications': notifications})                            