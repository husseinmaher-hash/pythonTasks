"""
BankAccount class 

Requirements:
1- Attributes
account_holder (required)
balance (required)
transaction_history 
(must be fully private and should not be accessed or modified from outside but it can accessed )

pin_code (must be fully private and cannot be accessed or modified from outside) 


2- Methods
deposit(amount) — adds money to the balance and records the transaction

withdraw(amount, pin) — subtracts money if PIN matches and records the transaction

show_balance(pin) — returns the current balance if PIN matches

show_transactions() — returns the transaction history

from_string(data_str) — class method that creates and returns a new BankAccount instance


validate_amount(amount) — static method that checks if an amount is valid


3- Validation & Encapsulation
Balance must be numeric and ≥ 0
PIN must be valid

4- Demonstrate
Create accounts using both the constructor and the class method

Perform deposits and withdrawals

Show that transaction_history and pin_code cannot be accessed from outside

Use the static method to validate amounts

"""

class BankAccount:
    """
        simple bank sestym that allow user to create account
        and deposit and withdrow from user account
        
    """
    def __init__(self,account_holder,balance ,pin_code = None ,transaction_history =[]):
        self.account_holder = account_holder
        if balance < 0 :
            raise Exception("Blease Enter the valid amount")
        self.balance = balance
        self._transaction_history = transaction_history
        if (type(pin_code) != int) and (len(str(pin_code)) != 4):
            raise Exception("the pin code must be int and four digit")
        
        self.__pin_code = pin_code
        self.transaction = transaction_history

    def deposit(self,amount):
        self.validate_amount(amount)
        self.balance += amount
        self.transaction.append(f"deposit {amount} to your account , your balance is{self.balance}")
    
    def withdraw(self,amount, pin):
        self.validate_amount(amount)
        if self.__pin_code != pin :
            raise Exception ("Error the pin numper is incorect")
        self.balance -= amount
        self.transaction.append(f"withdraw {amount} to your account , your balance is{self.balance}")

    def show_balance(self,pin):
        if self.__pin_code != pin :
            raise Exception ("Error the pin numper is incorect")
        return self.balance
    
    def show_transactions(self):
        print('\n',*self.transaction,sep='\n',end='\n\n')
    
    def from_string(self):
        self.account_holder = 'ALi'
        self.balance = 20000
        self.__pin_code = 5555

    @staticmethod
    def validate_amount(amount):
        if not(amount >= 0 and ((type(amount) == int) or (type(amount) == float) )):
            raise Exception("not valid amount ")

# case 1
hussein = BankAccount('hussein',1000000,1234)

#case 2 
jussein = BankAccount('',0)
jussein.from_string()
print(jussein.account_holder)



#case 3 
print("the balance before ddepsit :",hussein.balance)
hussein.deposit(20000)
print('the balance after deposit :', hussein.balance)




print('the balance before withdrow : ', hussein.balance)
hussein.withdraw(2000 ,1234 )
print('the balance  after withdrow : ', hussein.balance)



#case 4 
hussein.show_transactions()

try :
    print(hussein.__pin_code)

except Exception as e:
    print('cant access pin code for instant')



#case 5 
try :
    hussein.deposit(-20000)

except Exception as e:
    print('the amount shoud be positeve number ')
