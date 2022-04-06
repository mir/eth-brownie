from brownie import SimpleStorage, accounts, config

def test_deploy():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from" : account})
    got_value = simple_storage.retrieve()
    assert got_value == 0