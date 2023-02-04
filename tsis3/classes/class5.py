"""
Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. 
Withdrawals may not exceed the available balance. 
Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

"""

class Account:
    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance

    def deposit( self, number ):
        if ( number > int(self.balance) ) or ( number < 0 ):
            print( "You can not deposit" )
            return None
        self.balance = str( int(self.balance) - number )
        print( "Dear {}, {} succesfully deposit, your balance = {}".format(self.owner, number, self.balance) )

    def withdraw( self, number ):
        if ( number > int(self.balance) ) or ( number < 0):
            print( "You can not get withdraw" )
            return None
        self.balance = str( int(self.balance) - number )
        print( "Dear {}, {} succesfully withdrawal, your balance = {}".format(self.owner, number, self.balance) )

Account1 = Account( "Aziz" , 15000 )
Account1.deposit( 500000 )
Account1.deposit( 5000 )
Account1.withdraw( 4555 )
Account1.deposit ( -456 )
Account1.withdraw ( 156.564 )

