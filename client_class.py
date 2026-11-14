class Client:
    def __init__(self, name: str, balance: int):
        self.name = name
        self.balance = balance

    def can_afford( self, amount:int ) -> bool:
        if amount <= 0:
            return False
        if not self.can_afford(amount):
            return False
        self.balance -= amount
        return True

    def charge( self, amount:int ):
        if amount <= 0:
            return False
        if not self.can_afford(amount):
            return False
        self.balance += amount
        return True

    def topup( self, amount:int ):
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def __repr__(self):
        pass