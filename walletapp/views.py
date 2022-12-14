from django.shortcuts import render, redirect
from walletapp.models import Wallet
from . import forms
from . import models

# Create your views here.

# Start of Registrations
def register_customer(request):
    if request.method == 'POST':
        form = forms.CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CustomerRegistrationForm()    
    return render(request, "register_customer.html", {"form": form})
                                        
def register_wallet(request):
    if request.method == 'POST':
        form = forms.WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.WalletRegistrationForm()    
    return render(request, "register_wallet.html", {"form": form})

def register_currency(request):
    if request.method == 'POST':
        form = forms.CurrencyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CurrencyRegistrationForm()    
    return render(request, "register_currency.html", {"form": form}) 

def register_account(request):
    if request.method == 'POST':
        form = forms.AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.AccountRegistrationForm()    
    return render(request, "register_account.html", {"form": form}) 

def register_transaction(request):
    if request.method == 'POST':
        form = forms.TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.TransactionRegistrationForm()    
    return render(request, "register_transaction.html", {"form": form})

def register_card(request):
    if request.method == 'POST':
        form = forms.CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CardRegistrationForm()    
    return render(request, "register_card.html", {"form": form}) 

def register_thirdparty(request):
    if request.method == 'POST':
        form = forms.ThirdPartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.ThirdPartyRegistrationForm()    
    return render(request, "register_thirdparty.html", {"form": form}) 

def register_notifications(request):
    if request.method == 'POST':
        form = forms.NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.NotificationRegistrationForm()    
    return render(request, "register_notification.html", {"form": form})

def register_receipt(request):
    if request.method == 'POST':
        form = forms.ReceiptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.ReceiptRegistrationForm()    
    return render(request, "register_receipt.html", {"form": form}) 

def register_loan(request):
    if request.method == 'POST':
        form = forms.LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.LoanRegistrationForm()    
    return render(request, "register_loan.html", {"form": form})

def register_reward(request):
    if request.method == 'POST':
        form = forms.RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.RewardRegistrationForm()    
    return render(request, "register_reward.html", {"form": form})

# End of Registrations

# Start of Lists
                            
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
    return render(request, 'notifications_list.html',{'notifications': notifications})   
 
# End of Lists   

# Start of Single Object View

def customer_profile(request,id):
    customer = models.Customer.objects.get(id=id)
    return render(request, 'customer_profile.html',{'customer': customer})

def wallet_overview(request,id):
    wallet = models.Wallet.objects.get(id=id)
    return render(request, 'wallet_overview.html',{'wallet': wallet})

def  account_overview(request,id):
    account = models.Account.objects.get(id=id)
    return render(request, 'account_overview.html',{'account': account})

def  card_overview(request,id):
    card = models.Card.objects.get(id=id)
    return render(request, 'card_overview.html',{'card': card})

def  transaction_overview(request,id):
    transaction = models.Transaction.objects.get(id=id)
    return render(request, 'transaction_overview.html',{'transaction': transaction})

def  receipt_overview(request,id):
    receipt = models.Receipt.objects.get(id=id)
    return render(request, 'receipt_overview.html',{'receipt': receipt})   
                      
# End of Single Object View  

# Start of Edit Object View

def edit_customer(request,id):
    customer = models.Customer.objects.get(id=id)
    if request.method == 'POST':
        form = forms.CustomerRegistrationForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_profile', id=customer.id)
    else:
        form = forms.CustomerRegistrationForm(instance=customer)    
    return render(request, "edit_customer.html", {"form": form})


def edit_wallet(request,id):
    wallet = models.Wallet.objects.get(id=id)
    if request.method == 'POST':
        form = forms.WalletRegistrationForm(request.POST, instance=wallet)
        if form.is_valid():
            form.save()
            return redirect('wallet_overview', id=wallet.id)
    else:
        form = forms.WalletRegistrationForm(instance=wallet)    
    return render(request, "edit_wallet.html", {"form": form})

def edit_account(request,id):
    account = models.Account.objects.get(id=id)
    if request.method == 'POST':
        form = forms.AccountRegistrationForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('account_overview', id=account.id)
    else:
        form = forms.AccountRegistrationForm(instance=account)    
    return render(request, "edit_account.html", {"form": form})

def edit_card(request,id):
    card = models.Card.objects.get(id=id)
    if request.method == 'POST':
        form = forms.CardRegistrationForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('card_overview', id=card.id)
    else:
        form = forms.CardRegistrationForm(instance=card)    
    return render(request, "edit_card.html", {"form": form})

def edit_transaction(request,id):
    transaction = models.Transaction.objects.get(id=id)
    if request.method == 'POST':
        form = forms.TransactionRegistrationForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_overview', id=transaction.id)
    else:
        form = forms.TransactionRegistrationForm(instance=transaction)    
    return render(request, "edit_transaction.html", {"form": form})

def edit_receipt(request,id):
    receipt = models.Receipt.objects.get(id=id)
    if request.method == 'POST':
        form = forms.ReceiptRegistrationForm(request.POST, instance=receipt)
        if form.is_valid():
            form.save()
            return redirect('receipt_overview', id=receipt.id)
    else:
        form = forms.ReceiptRegistrationForm(instance=receipt)    
    return render(request, "edit_receipt.html", {"form": form})

# End of Edit Object View                  