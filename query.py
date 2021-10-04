# Command line interface to query the stock.

# To iterate the source data you can use the following structure:

# for item in warehouse1:
#     # Your instructions here.
#     # The `item` name will contain each of the strings (item names) in the list.


from data import warehouse1, warehouse2

user_name = input("Please, enter your name: ") #Here we ask user's name
LIST = 1
SEARCH= 2
QUIT = 3

print(f"Hello {user_name}!\nWhat would you like to do?:\n1. List items by warehouse\n2. Search an item and place an order\n3. Quit") #Here we show options

election = int(input("Type the number of the operation: ")) #User selects option

if election < 1 or election > 4: #Error if the input is != 1, 2 or 3
    print("Please, try again and enter a right option from 1 to 3")
#User select option 1   
elif election == LIST:                                                    
    print("Items warehouse 1: ",*warehouse2, sep="\n") #We show all items from first list
    print("Items warehouse 2: ", *warehouse2, sep="\n") #We show all items form second list
    print(f"Thank you for your visit, {user_name}")
#User select option 2
elif election == SEARCH:                                                  
    item = input("What is the name of the item?: ")  #User enter item's name
    if item in warehouse1 or item in warehouse2:
        print("Yey! We have this item")  #message if we have this item
        if item in warehouse1 and item in warehouse2: #We show in which list is
            print("Location: in both Warehouse.")
        elif item in warehouse1:
            print("Location: Warehouse 1.")
        elif item in warehouse2:
            print("Location: Warehouse 2") 
        count = warehouse1.count(item) + warehouse2.count(item) #We give user the amount available of the chosen item
        print(f"Amount available: {count}")                         
        buy = input("Would you like to order this item? (yes/no): ") #We ask h/h/t if wants to buy it
        if buy == "no": 
                print(f"Thank you for your visit, {user_name}")
        elif buy == "yes":                                             
                amount = int(input("How many would you like?: ")) #We ask the amount h/h/t wants to buy
                if amount == count or amount < count:
                    print(f"{amount} {item} have been ordered.")
                else:
                    print(f"There are not this many available. The maximun amount that can be ordered is {count}.")
                    buy_amount_available = input("Would you like to order the maximum available?(yes/no): ")   #We give the posibility to buy the amount available.
                    if buy_amount_available == "yes":
                        print(f"{count} {item} have been ordered.\nThank you for your visit {user_name}")
                    else:
                        print(f"Thank you for you visit, {user_name}")
        else:
            print("Please, enter yes or no")                                #User does not want to buy selected item
    else:
        print(f"Not in stock.\nThank you for your visit, {user_name}") 
#User selection option 3    
else:
    print(f"Thank you for your visit, {user_name}") 
     
           








   




# YOUR CODE STARTS HERE

# Get the user name

# Greet the user

# Show the menu and ask to pick a choice

# If they pick 1
#
# Else, if they pick 2
#
# Else, if they pick 3
#
# Else

# Thank the user for the visit
