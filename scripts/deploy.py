from brownie import accounts, config, SimpleStorage
import os

def deploy_contract():
    # account = accounts.add(config["wallets"]["from_key"])
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)

def main():
    deploy_contract()