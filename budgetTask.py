class Budget:

  def __init__(self, category, amount): # class attributes
    self.category = category
    self.amount = amount

# class methods
  def deposit(self):
    depositAmount = float(input('How much would you like to deposit?\n'))
    self.newBalance = depositAmount + self.amount
    return self.newBalance


  def withdrawal(self):
    withdrawAmount = float(input('How much would you like to withdraw?\n'))
    self.newBalance = self.amount - withdrawAmount
    return self.newBalance


  def get_balance(self):
    print('Your current balance is %d' % self.newBalance)

  def transfer(self):
    transferOptions = int('what do you want to do? 1. option1 2. option2')
    if transferOptions == 1:
      return self.deposit()
    else:
      return self.withdrawal()

    print(self.newBalance)

#I still don't understand how to do this transfer part      

    
    

    


food = Budget('Food', 3000)

clothing = Budget('Clothing', 2500)

entertainment = Budget('Entertainment', 1000)

salary = Budget('Salary', 9000)

food.withdrawal()
food.get_balance()


