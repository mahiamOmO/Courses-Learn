def create_food_price_dict(food_list, price_list):
    food_price_dict = {}
    for i in range(len(food_list)):
        if price_list[i] <= 1000:  # Filtering out foods with prices above 1000 taka
            food_price_dict[food_list[i]] = price_list[i]
    return food_price_dict

# Example lists
food_list = ["Rice", "Chicken", "Steak"]
price_list = [30, 120, 1500]

# Calling the function and printing the result
food_price_dict = create_food_price_dict(food_list, price_list)
print(food_price_dict)
