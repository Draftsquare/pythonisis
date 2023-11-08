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
        ["Hersheys", 2.99],
        ["Sourpatch kids", 1.99],
        ["Jolly ranchers", 2.89 ],
    ],
    [ 
        ["Hersheys", 2.99],
        ["Sourpatch kids", 1.99],
        ["Jolly ranchers", 2.89 ],
    ],[ 
        ["Hersheys", 2.99],
        ["Sourpatch kids", 1.99],
        ["Jolly ranchers", 2.89 ],
    ],

    
]

# ["Lays", "Doritos", "Pop corners" ],
# ["Gatorade", "Coca Cola", "Pepsi" ],
# ["Steam", "Amazon", "Gamestop" ]

WantsToShop = True


while WantsToShop == True:
        print("Categories:")
        for index, category in enumerate(categories):
            print(f"{category}")

        category_choice = int(input("Select a category (1-4):") or 0) - 1
        if 0 <= category_choice < len(categories):
            print(f"Items in the '{categories[category_choice]}' category:")
            for item in items[category_choice]:
                print(f"- {item}")

        else:
                print("Invalid category choice. Please choose a number between 1 and 4.")
        user_input = input("Continue shopping? (y/n): ")
        if user_input.lower() == "n":
              WantsToShop = False
              print("Exiting the program.")
