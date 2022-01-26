from brownie import FundMe, config, accounts
from scripts.helpful_scripts import get_account

def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    fund_me.fund({"from":account, "value":entrance_fee})

def withdraw():
    withdraw_me = FundMe[-1]
    account = get_account()
    withdraw_me.withdraw({"from":account})
    
def main():
    fund()
    withdraw()