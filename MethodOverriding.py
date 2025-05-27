class CreditCardPayment:
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")
        super().pay(amount)

class PayPalPayment:
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

class OnlineStore(CreditCardPayment, PayPalPayment):
    pass

store = OnlineStore()
store.pay(100)  

print(OnlineStore.__mro__)# MRO determines which 'pay' method is called