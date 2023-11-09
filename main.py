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
    ],
    
    [ 
        ["Steam", 20],
        ["Amazon", 25],
        ["Gamestop", 50 ],
    ],
    
]



# ["Lays", "Doritos", "Pop corners" ],
# ["Gatorade", "Coca Cola", "Pepsi" ],
# ["Steam", "Amazon", "Gamestop" ]
userChoice = input()
userChoiceIndex = int(userChoice) - 1
cart = []
wantsToShop = True # assuming the user wants shop

# currentItem = 1
# for category in categories:
#     print( f"{currentItem}. {category}" )
#     currentItem = currentItem + 1

print( "\nHere are the list of categories: \n" )


for currentCategoryIndex in range( len( categories ) ):
    print( f"{currentCategoryIndex + 1}. {categories[ currentCategoryIndex ]}" )

userCategory = input( "\nPlease enter your category number: " ) # the input function will always return a string
userCategory = int(userCategory) # and so we need to covert it to a number (int) if we want it as a number
userCategoryIndex = userCategory - 1 

print( f"\nGreat choice, you selected {categories[ userCategoryIndex ]}. Here are all the items.\n" )
userCategoryItems = items[ userCategoryIndex ] # This is the list of items in the category the user selected

for currentItemDetailsIndex in range( len( userCategoryItems ) ):
    print( f"{currentItemDetailsIndex +1}. {userCategoryItems[ currentItemDetailsIndex] [0]}." )






