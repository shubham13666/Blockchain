
# iterating  over each transaction in each block on the chain to search for the public key

def get_balance(self, address):
    balance = 0
    for block in self.blocks:
        for transaction in block.transactions:
            if transaction["from"] == address:
                balance -= transaction["amount"]
            if transaction["to"] == address:
                balance += transaction["amount"]
    return balance




ob.get_ba