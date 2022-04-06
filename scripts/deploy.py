from brownie import accounts, config, SimpleStorage
import os

def deploy_contract():
    # account = accounts.add(config["wallets"]["from_key"])
    account = accounts[0]    
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