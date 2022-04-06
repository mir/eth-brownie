from brownie import accounts, config, SimpleStorage, network
import os

def get_account():
    if (network.show_active() == 'development'):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_contract():
    account = get_account()    
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)    
    stored_value = simple_storage.retrieve()
    print(f"Stored value is {stored_value}")
    transaction = simple_storage.store(15,{"from": account})
    transaction.wait(1)
    stored_value = simple_storage.retrieve()
    print(f"Stored value is {stored_value}")


def main():
    deploy_contract()