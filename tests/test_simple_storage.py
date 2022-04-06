from brownie import SimpleStorage, accounts, config

def test_deploy():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from" : account})
    got_value = simple_storage.retrieve()
    assert got_value == 0

def test_update_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    TEST_VALUE = 15
    simple_storage.store(TEST_VALUE, {"from" : account})
    got_value = simple_storage.retrieve()
    assert got_value == TEST_VALUE