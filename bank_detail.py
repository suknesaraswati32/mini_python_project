class BankAccount:
      def __init__(self, account_holder):
          self.account_holder = account_holder
          self.account_number = self.generate_account_number()
          self.balance = 0.0
      def deposite(self,amount):
           if amount>0:
               self.balance+=amount
               print(amount,"deposited successfully.")
               
      def withdraw(self,amount):
          if amount<=0:
              print("Invalid withdrawal amount.")
          elif self.balance>=amount:
              self.balance-=amount
              print(amount,"withdrawn successfully.")
          else:
              print("Error: Insufficient funds.")
      def display_balance(self):
          print("Current Balance:",self.balance) 
      def transfer(self,amount,other_account):         
          if amount<=0:
              print("Invalid transfer amount.")
          elif self.balance>=amount:
              self.balance-=amount
              other_account.balance+=amount
              print(amount,"transferred successfully from",self.account_holder,"to",other_account.account_holder)
          else:
              print("Error: Insufficient funds for transfer.")
             
account1=BankAccount("Rahul")             
account1.deposite(10000)     
account1.display_balance()        