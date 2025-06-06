# FILE: account.py 
# 
# SUBJECT: Classes representing different types of accounts
#
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-02-05
# 

class BankAccount:
    owner = None
    balance = 0.0
    # dummy data attribute to be used by children only (with according values)
    interest = 0.01 
    
    # just for development/testing
    
    _debug = False
    
    def __init__(self, owner: str, dpt_amt=None) -> None:
        if self._debug:
            print(self.__class__)
        self.owner = owner
        if dpt_amt != None:
            self.deposit(dpt_amt)
    
    def deposit(self, amount: float) -> None:
        if self._debug:
            print('+ {}'.format(amount))
        self.balance += abs(amount)
    
    def withdraw(self, amount: float) -> None:
        if self._debug:
            print('- {}'.format(amount))
        self.balance -= abs(amount)
    
    def get_balance(self) -> float:
        """ Rounding just the balance, calculating precisily

        Returns:
            float: current balance "Saldo"
        """
        return round(self.balance, 2)
    
    def calc_interest(self, days=0) -> float:
        """ Allowed for children only!! """
        if str(self.__class__).find('BankAccount') != -1:
            raise TypeError('No interest with this type of account 😢')
        return self.get_balance() * self.interest * days / 365
    
    def set_debug(self, flag: bool) -> None:
        self._debug = flag
        
    def __str__(self) -> str:
        return f'{self.owner} :: balance: {self.get_balance()}'
        
class PrimeAccount(BankAccount):
    """ Prime Account with interest

    Args:
        BankAccount (_type_): _description_
    """
    interest = 0.02

    def apply_interest(self, days: int) -> None:
          self.balance += self.calc_interest(days)
    

    
class SavingsAccount(BankAccount):
    """ Special account with nice interst, but blocked until cut-off  
        date(not implemented yet)   
    """
    blocked = True
    interest = 0.05
    pass
    def apply_interest(self, days) -> None:
        self.balance += self.calc_interest(days)
        
    def unblock_account(self) -> None:
        self.blocked = False    
        if self._debug:
            print('Account was unblocked!')
    
    def withdraw(self, amount: float) -> None: 
        if self.blocked:
            raise LookupError('This account is still blocked! - 😢')
        else: super().withdraw(amount)

class WasteFulAccount(BankAccount):
    """ Demo account type for testing """
    interest = 0.12
