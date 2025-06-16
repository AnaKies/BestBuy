class Product:
    def __init__(self, name, price, quantity):
        if not name or name == '':
            raise ValueError("Name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.name = name
        try:
            self.price = float(price)
        except Exception:
            raise ValueError("Price must be a decimal number")

        try:
            self.quantity = int(quantity)
        except Exception:
            raise ValueError("Quantity must be a number")
        self.active = True

    def get_quantity(self):
        """
        Getter function for quantity. Returns the quantity (int).
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Setter function for quantity. If quantity reaches 0, deactivates the product.
        """
        self.quantity = quantity
        # make product unavailable
        if self.quantity == 0:
            self.active = False
        # activate product available again
        if self.quantity > 0:
            self.active = True

    def is_active(self):
        """
        Getter function for active. Returns True if the product is active, otherwise False.
        """
        return self.active

    def activate(self):
        """
        Activates the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product.
        """
        self.active = False

    def show(self):
        """
        Returns a string that represents the product
        """
        product_info = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        print(product_info)

    def buy(self, quantity):
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        """
        if not self.active:
            raise ValueError("Product is not available")

        if quantity > self.quantity:
            raise ValueError("Quantity cannot be greater than product quantity")
        # reduce the initial quantity
        self.set_quantity(self.quantity - quantity)
        # total price of the bought items
        total_price = float(self.price * quantity)
        return total_price

def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

if __name__ == "__main__":
    main()
