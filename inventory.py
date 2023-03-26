# importing libraries, requires install
from tabulate import tabulate


# defining classes
class Shoe:
    """
        This class represents a Shoe object with attributes for country, code,
        product, cost, and quantity. The class also has methods for retrieving
        the cost and quantity of a Shoe object.
        """
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return [self.country, self.code, self.product, self.cost,
                self.quantity]


# initialising list that will store shoe objects
shoe_list = []


# defining functions
def read_shoes_data():
    """Reads the shoe data from a file 'inventory.txt' and appends the
       data to a list of Shoe objects. If the file read is successful, it
       prints a success message. In case of an error, it prints an
       unsuccessful reading message.
       """
    try:
        with open("inventory.txt", "r") as f:
            # skips the first line, grabs the data with a for loop
            # creates an object of the Shoe class with that data
            # appends the object to shoe_list
            next(f)
            for line in f:
                country, code, product, cost, quantity = \
                    line.strip().split(",")
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
            print("\nFile read successfully.")
    except FileNotFoundError:
        print("Unsuccessful reading file")


def assign_shoes():
    """Accepts input from the user to create a Shoe object, which is then
      appended to the list of Shoe objects. If the inputs for cost and
      quantity are not numbers, it raises a ValueError.
      """
    while True:
        try:
            country = input("Enter country: ")
            code = input("Enter code: ")
            product = input("Enter product: ")
            cost = float(input("Enter cost: "))
            quantity = int(input("Enter quantity: "))
            shoe = Shoe(country, code, product, cost, quantity)
            shoe_list.append(shoe)
            print("\nProduct entered.")
            break
        except ValueError:
            print("\nOnly enter numbers for 'quantity' and 'cost'.")


def view_all():
    """Prints the details of all Shoe objects in a table format.
       """
    # set out the format for the table in list format
    # initialise empty list
    # for each object in the shoe_list append them to the new list as strings
    # print the new list using the tabulate function
    head = ["Country", "Code", "Product", "Cost", "Quantity"]
    shoe_string_list = []
    for shoe in shoe_list:
        shoe_string_list.append(shoe.__str__())
    print(tabulate(shoe_string_list, headers=head, tablefmt="grid"))


def re_stock():
    """Finds the Shoe object with the minimum quantity and allows the user
        to enter a quantity to add to the stock. It then updates the stock
        level and writes the updated data to the file 'inventory.txt'.
        """
    # Set the minimum quantity to a large number for comparison
    # Initialize a variable to store the shoe with the minimum quantity
    min_quantity = 999999
    shoe_to_restock = None

    # Loop through each shoe in the shoe list
    # If the shoe's quantity is less than the current minimum quantity
    # Update the minimum quantity and store the shoe with the minimum quantity
    for shoe in shoe_list:
        if int(shoe.get_quantity()) < int(min_quantity):
            min_quantity = shoe.get_quantity()
            shoe_to_restock = shoe

    # If a shoe with the minimum quantity was found
    # Ask the user to enter a quantity to add to the stock
    # Add the quantity entered by the user to the shoe's stock
    # Print the updated stock level
    if shoe_to_restock:
        add_qty = int(
            input(f"Re-stock {shoe_to_restock.product}, Stock: "
                  f"{shoe_to_restock.quantity}? Enter quantity: "))
    shoe_to_restock.quantity = int(shoe_to_restock.quantity) + int(add_qty)
    print(f"The stock level has been updated to: {shoe_to_restock.quantity}")

    # Write the updated data to the file 'inventory.txt'
    with open("inventory.txt", "w") as f:
        f.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoe_list:
            f.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},"
                    f"{shoe.quantity}\n")


def search_shoe():
    """Accepts a product code from the user and searches for a Shoe
       object with that code. If found, it returns the details of the Shoe
       object. If not found, it returns a message that the product code was
       not found.
       """
    # asks the user for the product code and iterates through the list of
    # Shoe objects, if the user code == the object code, it prints the product.
    # if the code is not found, prints an error message.
    while True:
        code = input("Enter code: ")
        for shoe in shoe_list:
            if shoe.code == code:
                return f"""\nThe product you requested is printed below:
                    
    Country:    {shoe.country}
    Code:       {shoe.code}
    Product:    {shoe.product}
    Cost:       R{shoe.cost}
    Quantity:   {shoe.quantity}
    """

        return "\nSorry I cannot find that product code, please try again."


def value_per_item():
    """Calculates the value of each Shoe object in the list by multiplying
       the cost and quantity and returns the result in a table format.
       """
    # iterating through the list of objects, the code runs the value calc
    # and appends the answer along with the object name to a new value_list
    # then using tabulate it generates a neat table from this new list.
    value_list = []
    for shoe in shoe_list:
        value = int(shoe.get_cost()) * int(shoe.get_quantity())
        value_list.append([shoe.product, "R" + value.__str__()])
    print(tabulate(value_list, headers=["Product", "Value"], tablefmt="grid"))


def highest_qty():
    """Finds the Shoe object with the highest quantity and returns the
        name of the product.
        """
    # Finds the product with the highest stock value, each time the loop
    # iterates the max_quantity variable is updated IF it's > than the previous
    # value, and the object value is stored in the max_shoe variable. Once
    # the loop has finished it prints the object with the highest quantity.
    max_quantity = 0
    for shoe in shoe_list:
        if int(shoe.get_quantity()) > int(max_quantity):
            max_quantity = shoe.get_quantity()
            max_shoe = shoe
    print(f"{max_shoe.product} is for sale")


# ==========Main Menu=============
# displays a menu, depending on the input, it either runs a specific function
# or a ValueError is excepted and an error message is printed, to break out of
# the loop option 8 is required.
while True:
    try:
        choice = int(input("""\nMain Menu:
    1. Read Shoes Data
    2. Assign Shoes
    3. View All Shoes
    4. Re-stock Shoes
    5. Search Shoes
    6. Value per Item
    7. Highest Quantity
    8. Quit
        
    Choice: """))

        if choice == 1:
            read_shoes_data()
        elif choice == 2:
            read_shoes_data()
            assign_shoes()
        elif choice == 3:
            read_shoes_data()
            view_all()
        elif choice == 4:
            read_shoes_data()
            re_stock()
        elif choice == 5:
            read_shoes_data()
            view_all()
            print(search_shoe())
        elif choice == 6:
            read_shoes_data()
            value_per_item()
        elif choice == 7:
            read_shoes_data()
            highest_qty()
        elif choice == 8:
            print("Goodbye!")
            break
        else:
            print("Only enter numbers between 1 and 8. Please try again.")
    except ValueError:
        print("Please only enter numbers between 1 and 8.")
