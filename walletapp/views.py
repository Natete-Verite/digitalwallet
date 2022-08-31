from django.shortcuts import render
from walletapp.models import Wallet
from .forms import AccountRegistrationForm, CardRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationRegistrationForm, ReceiptRegistrationForm, RewardRegistrationForm, ThirdPartyRegistrationForm, TransactionRegistrationForm
from .forms import WalletRegistrationForm
from .forms import CurrencyRegistrationForm

# Create your views here.
def register_customer(request):
    form = CustomerRegistrationForm()
    return render(request, "register_customer.html", {"form": form})
                                        
def register_wallet(request):
    form = WalletRegistrationForm()
    return render(request, "register_wallet.html", {"form": form})   

def register_currency(request):
    form = CurrencyRegistrationForm()
    return render(request, "register_currency.html", {"form": form}) 

def register_account(request):
    form = AccountRegistrationForm()
    return render(request, "register_account.html", {"form": form}) 

def register_transaction(request):
    form = TransactionRegistrationForm()
    return render(request, "register_transaction.html", {"form": form}) 

def register_card(request):
    form = CardRegistrationForm()
    return render(request, "register_card.html", {"form": form}) 

def register_thirdparty(request):
    form = ThirdPartyRegistrationForm()
    return render(request, "register_thirdparty.html", {"form": form}) 

def register_notifications(request):
    form = NotificationRegistrationForm()
    return render(request, "register_notifications.html", {"form": form}) 

def register_receipt(request):
    form = ReceiptRegistrationForm()
    return render(request, "register_receipt.html", {"form": form}) 

def register_loan(request):
    form = LoanRegistrationForm()
    return render(request, "register_loan.html", {"form": form}) 

def register_reward(request):
    form = RewardRegistrationForm
    return render(request, "register_reward.html", {"form": form}) 
                                     