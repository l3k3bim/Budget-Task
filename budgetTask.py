class Budget:

  def __init__(self, category): # class attributes
    self.category = category
    self.amount = 1000

# class methods
  def deposit(self, amount):
    
    self.amount += amount
    return self.amount


  def withdrawal(self, amount):
    
    self.amount -= amount
    return self.amount


  def get_balance(self, amount):
    if self.amount < amount:
      return False
    else:
      return True
    

  def transfer(self, amount, category):
    if self.get_balance(amount) == True:
      self.amount -= amount
      category.amount += amount
      return "You have transferred from one category to another"
    else:
      return "You have insufficient balance"  
   

category = Budget("Clothing")

print("This is a deposit for clothing", category.deposit(800))
#print("This is a withdrawal for clothing", category.withdrawal(200))

category_1 = Budget("food")
print("This is a deposit for food", category.deposit(1000))
print(category_1.get_balance(400))

print(category_1.transfer(600, category))



