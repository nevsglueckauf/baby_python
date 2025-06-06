import unittest
import account

class TestAccounts(unittest.TestCase):
    """ Unit testing Acccount types

    Args:
        unittest (_type_): _description_
    """
    def test_bank_account(self):
        pp_acc = account.BankAccount('Peter Parker', 2300)
        self.assertEqual(pp_acc.get_balance(), 2300)
        self.failureException()
        self.assertRaises(Exception, pp_acc.calc_interest, 366)
        
        pp_acc.deposit(33.32)
        self.assertEqual(pp_acc.get_balance(), 2333.32)
        
    def test_bank_account_movements(self):
        pp_acc = account.BankAccount('Clint Barton', 2300)
        self.assertEqual(pp_acc.get_balance(), 2300)
        pp_acc.deposit(33.32)
        self.assertEqual(pp_acc.get_balance(), 2333.32)
    
    def test_savings_account(self):
        dd_acc = account.SavingsAccount('Daisy Duck', 1000)
        self.assertEqual(1000, dd_acc.get_balance())
        
    
    def test_savings_account_movements(self):
        dd_acc = account.SavingsAccount('Uncle Scrooge', 1000)
        self.assertRaises(LookupError, dd_acc.withdraw, 366)
        
    def test_savings_account_unblocking(self):
        madame_web_acc = account.SavingsAccount('Agatha Harkness', 1000)
        madame_web_acc.unblock_account()
        madame_web_acc.withdraw(100)
        self.assertEqual(900, madame_web_acc.get_balance())
    
    def test_savings_account_interest(self):
        dd_acc = account.SavingsAccount('Daisy Duck', 1000)
        foo = dd_acc.get_balance()
        dd_acc.apply_interest(360)
        self.assertTrue(dd_acc.get_balance() > foo)
        self.assertIsInstance(str(dd_acc), str)
        self.assertTrue(str(dd_acc).find('Daisy Duck') != -1)
        
    def test_savings_account_stringification(self):
        dd_acc = account.SavingsAccount('Daisy Duck', 1000)
        self.assertIsInstance(str(dd_acc), str)
        self.assertTrue(str(dd_acc).find('Daisy Duck') != -1)
        
        
if __name__ =='__main__':
    unittest.main()
    
dd_acc = account.SavingsAccount('Daisy Duck', 1000)
print(dd_acc)
 