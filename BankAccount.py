class BankAccount:
  def __init__(self): 
    self.__nextAccountNumber : int
    self.__accountNumber : int
    self.__accountName : str
    self.__balance : int
    self.__availabelBalance : int
    self.__overdraftLimit :int

  def open(self,accountName):
    self.__accountName = accountName;
    self.__balance = 1; 
    self.__accountNumber = 1;
    self.__availableBalance = 100;
    self.__overdraftLimit = 300;
    return True;
  def close(self): return True;
  def credit(self,amount): return True;
  def debit(self,amount): return True;
  def viewBalance(self): return self.__balance;
  def viewCredit(self): return self.__availableBalance  
  def viewDebit(self): return self.__overdraftLimit 
  def _getBalance(self): return self.__balance;
  def __setBalance(self, newBalance):
    self.__balance = newBalance;
  def _getAccountName(self):
    return self.getAccountName();
  def _setAccountName(self, newName):
    self.__accountName = newName;  return True;
 