import products
import store


def print_menu():
    """
    Displays the menu.
    """
    print("""\nStore Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
""")


def list_all_products(product_store):
    """
    List all products in store.
    """
    all_products_in_store = product_store.get_all_products()

    print("------")

    for index, product in enumerate(all_products_in_store):
        print(f"{index + 1}. {product.show()}")

    print("------")


def show_total_products(product_store):
    """
    Show the total amount of products in store.
    """
    all_products_list = product_store.get_total_quantity()
    print(f"Total of {all_products_list} items in store")


def place_order(product_store):
    """
    Place an order.
    """
    try:
        order_list = []
        list_of_all_active_products_in_store = product_store.get_all_products()
        print("When you want to finish order, enter empty text.")

        while True:
            user_order = input("Which product # do you want? ").strip()
            if user_order == "":
                break
            user_amount = input("What amount do you want? ")

            try:
                # decrement, because the index in menu starts at 1
                product_index = int(user_order) - 1
                chosen_product = list_of_all_active_products_in_store[product_index]
                order_list.append((chosen_product, int(user_amount)))
            except (ValueError, TypeError):
                raise ValueError("Invalid input")
            except Exception as error:
                print(f"Error placing order: {error}")

            print("Product added to list!\n")

        if not order_list:
            print("No products were placed in the order list.")
            return

        total_price = product_store.order(order_list)
        print(f"Order made! Total payment: ${total_price}")

    except Exception as error:
        print(f"Error adding product!: {error}")


def get_user_choice():
    """
    Returns the user choice.
    """
    while True:
        try:
            user_input = int(input("Please choose a number: "))
            return user_input
        except (ValueError, TypeError):
            print("Error with your choice! Try again!")


def start(product_store):
    """
    Handle the menu and users choice.
    """
    menu_func = {1: list_all_products,
                 2: show_total_products,
                 3: place_order}

    while True:
        print_menu()
        try:
            user_choice = get_user_choice()

            if user_choice == 4:
                break

            menu_func[user_choice](product_store)
        except Exception as error:
            print(error)


def main():
    """
    Initialise the stock of the store
    """
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
