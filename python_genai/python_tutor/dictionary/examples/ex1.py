accounts = {101: 40000, 102: 25000, 103: 32000}
acct_id = int(input("Enter account ID: "))
amount = int(input("Enter amount to withdraw: "))

balance = accounts.get(acct_id, None)
if balance is None:
    accounts[acct_id] = amount
    print("Account added.")

