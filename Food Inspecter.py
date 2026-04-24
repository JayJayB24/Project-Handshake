foods = {
    "chips": ["potatoes", "salt", "oil"],
    "milk": ["milk", "vitamin d"],
    "peanut butter": ["peanuts", "salt", "sugar"],
    "bread": ["wheat", "yeast", "salt"],
    "pizza": ["dough", "cheese", "tomato sauce"],
    "burger": ["beef", "bun", "lettuce", "cheese"],
    "hotdog": ["meat", "bun", "salt"],
    "ice cream": ["milk", "sugar", "cream"],
    "cereal": ["grains", "sugar", "vitamins"],
    "chocolate": ["cocoa", "sugar", "milk"],
    "apple": ["apple"],
    "banana": ["banana"],
    "orange": ["orange"],
    "yogurt": ["milk", "bacteria", "sugar"],
    "cheese": ["milk", "salt", "enzymes"],
    "eggs": ["eggs"],
    "pasta": ["wheat", "water"],
    "chicken nuggets": ["chicken", "bread crumbs", "oil"],
    "fries": ["potatoes", "salt", "oil"]
}

food_name = input("Enter a food to check: ").lower()

if food_name in foods:
    print("\nIngredients in", food_name + ":")
    
    for ingredient in foods[food_name]:
        print("-", ingredient)
    
    allergy = input("\nDo you have an allergy? Type it (or type 'no'): ").lower()
    
    if allergy != "no":
        if allergy in foods[food_name]:
            print("Warning: This food contains any allergic reactions", allergy)
        else:
            print("This food does NOT contain any allergic reactions", allergy)
    else:
        print("No allergy check needed.")
else:
    print("Food not found in system.")