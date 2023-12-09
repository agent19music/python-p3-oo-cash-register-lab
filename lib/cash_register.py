#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount= 0):
    self.discount = discount
    self.items =[]
    self.total = 0
    self.previous_transactions = []
  pass
 
  def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        for x in range(quantity):
            self.items.append(item)
        self.previous_transactions.append(
            {"item": item, "quantity": quantity, "price": price}
        ) 

  def apply_discount(self):
       if self.discount != 0 and self.discount > 0:
            self.total = int(self.total - (self.total * (self.discount / 100)))
            print(f"After the discount, the total comes to ${self.total}.")
       else:
            print("There is no discount to apply.")

  def void_last_transaction(self):
        if not self.previous_transactions:
            return "There are no transactions to void."
        self.total -= (
            self.previous_transactions[-1]["price"]
            * self.previous_transactions[-1]["quantity"]
        )
        for x in range(self.previous_transactions[-1]["quantity"]):
            self.items.pop()
        self.previous_transactions.pop()          
      
      