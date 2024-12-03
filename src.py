import pandas as pd

# Load or create a food database
try:
    # Attempt to load existing food data
    food_df = pd.read_csv('calories.csv')
except FileNotFoundError:
    # If the file doesn't exist, create a default database
    data = {
        "Food": ["Apple", "Banana", "Rice", "Chicken Breast", "Salmon", "Bread"],
        "Calories_per_100g": [52, 89, 130, 165, 208, 265]
    }
    food_df = pd.DataFrame(data)
    food_df.to_csv('food_data.csv', index=False)

def log_meal():
    """
    Log a meal by entering food items and their weights.
    """
    meal = []
    while True:
        food_item = input("Enter food item (or 'done' to finish): ").strip()
        if food_item.lower() == 'done':
            break
        weight = float(input(f"Enter weight of {food_item} in grams: ").strip())
        meal.append((food_item, weight))
    return meal

def calculate_calories(meal):
    """
    Calculate total calories from the meal.
    """
    total_calories = 0
    for food, weight in meal:
        match = food_df[food_df["Food"].str.lower() == food.lower()]
        if not match.empty:
            calories = (match["Calories_per_100g"].values[0] * weight) / 100
            total_calories += calories
        else:
            print(f"Food item '{food}' not found in database.")
    return total_calories

def main():
    print("Welcome to the Food Calorie Tracker!")
    while True:
        print("\nOptions:")
        print("1. Log a meal")
        print("2. View food database")
        print("3. Exit")
        
        choice = input("Choose an option: ").strip()
        if choice == '1':
            meal = log_meal()
            total_calories = calculate_calories(meal)
            print(f"Total Calories Consumed: {total_calories:.2f} kcal")
        elif choice == '2':
            print("\nFood Database:")
            print(food_df)
        elif choice == '3':
            print("Exiting the tracker. Stay healthy!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
