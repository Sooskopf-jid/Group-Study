class Client:
    def __init__(self, name: str, balance: int):
        self.name = name
        self.balance = balance

    def can_afford( self, amount:int ) -> bool:
        pass

    def charge( self, amount:int ):
        pass

    def topup( self, amount:int ):
        pass

    def __repr__(self):
        pass