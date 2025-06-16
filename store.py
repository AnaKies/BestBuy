import products


class Store:
    def __init__(self, list_of_products):
        self.list_of_products = list_of_products

    def add_product(self, product):
        """
        Add a product to the store.
        """
        if isinstance(product, products.Product):
            self.list_of_products.append(product)

    def remove_product(self, product):
        """
        Removes a product from store.
        """
        if product in self.list_of_products:
            self.list_of_products.remove(product)
        else:
            raise ValueError(f"Error: Product {product.name} not found")

    def get_total_quantity(self):
        """
        Returns how many items are in the store in total.
        """
        total_items = 0
        for product in self.list_of_products:
            total_items += product.quantity
        return total_items

    def get_all_products(self):
        """
        Returns all products in the store that are active.
        """
        active_products_list = []

        for product in self.list_of_products:
            if product.active:
                active_products_list.append(product)
        return active_products_list

    def order(self, shopping_list):
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        """
        try:
            total_price = 0
            for order in shopping_list:
                product, quantity = order
                total_price += product.buy(quantity)

            return total_price
        except Exception as error:
            raise Exception(error)


def main():
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = products.Product("MacBook Air M2", price=1450, quantity=100)

    best_buy = Store([bose, mac])
    price = best_buy.order([(bose, 5), (mac, 30), (bose, 10)])
    print(f"Order cost: {price} dollars.")

    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    my_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(my_products[0], 1), (my_products[1], 2)]))


if __name__ == "__main__":
    main()
