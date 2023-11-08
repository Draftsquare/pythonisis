categories = [
    "Candy",
    "Chips",
    "Drinks",
    "Giftcards"
]

items = [
    [ 
        ["Hersheys", 2.99],
        ["Sourpatch kids", 1.99],
        ["Jolly ranchers", 2.89 ],
    ],
    [ 
        ["Lays", 2.49],
        ["Doritos", 2.69],
        ["Popcorners", 2.39 ],
    ],
    [ 
        ["Gatorade", 2.49],
        ["Coca-Cola", 2.69],
        ["Pepsi", 1.48 ],
    ],[ 
        ["Steam", 20],
        ["Amazon", 25],
        ["Gamestop", 50 ],
    ],

    
]

# ["Lays", "Doritos", "Pop corners" ],
# ["Gatorade", "Coca Cola", "Pepsi" ],
# ["Steam", "Amazon", "Gamestop" ]

wantsToShop = True


while wantsToShop:
        print("Categories:")
        for index, category in enumerate(categories):
            print(f"{category}")

        category_choice = int(input("Select a category (1-4):") or 0) - 1
        
        if 0 <= category_choice < len(categories):
            print(f"Items in the '{categories[category_choice]}' category:")
            for item in items[category_choice]:
                print(f"{item}")

            shopping_cart = []

            while True:
                item_choice = int(input("Select an item (1-3):")) - 1

                if 0 <= item_choice < len(items[category_choice]):
                        selected_item = items[category_choice][item_choice]
                        shopping_cart.append(selected_item)
                        print(f"'{selected_item}' added to the cart.")
                else:
                        print("Invalid item choice. Please select a valid item.")

                another_item = input("Select another item in this category? (y/n). You can also press 'c' to check outm or 'v' to view the cart:").lower()
                if another_item == "c":
                      # User chose to check out
                      break
                elif another_item == "v":
                      # User wants to view the cart
                      print("Items in your shopping cart:")
                      for item in shopping_cart:
                            print(f"'{item}")
                elif another_item != "y":
                      break #Exits the item selection loop if user is done
                
            total_price = 0 #Initialize the total price to 0
            for item in shopping_cart:
                total_price += calculate_price(item)

            print("items in your shopping cart:")
            for item in shopping_cart:
                print(f"'{item}")

            print(f"Total Price: ${total_price: .2f}")
                       
                  
            else:
            print("Invalid category choice. Please choose a number between 1 and 4.")

            

            
                       
                        


        else:
                print("Invalid category choice. Please choose a number between 1 and 4.")
        user_input = input("Continue shopping? (y/n): ")
        if user_input.lower() == "n":
              wantsToShop = False
              print("Exiting the program.")
