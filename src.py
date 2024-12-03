import json

class FoodCalorieTracker:
    def __init__(self, data_file="calorie_data.json"):
        self.food_items = []
        self.data_file = data_file
        self.load_data()

    def add_food(self, food_name, calories):
        """
        Add a food item and its calorie count.
        :param food_name: Name of the food item.
        :param calories: Number of calories (integer).
        """
        try:
            calories = int(calories)
            self.food_items.append({'name': food_name, 'calories': calories})
            print(f"Added: {food_name} - {calories} calories.")
        except ValueError:
            print("Error: Calories must be a number.")

    def view_food_items(self):
        """Display all food items and their calorie counts."""
        if not self.food_items:
            print("No food items recorded yet.")
            return
        print("\n--- Food Items ---")
        for idx, item in enumerate(self.food_items, 1):
            print(f"{idx}. {item['name']} - {item['calories']} calories")
        print("------------------")

    def total_calories(self):
        """Calculate and display the total calories consumed."""
        total = sum(item['calories'] for item in self.food_items)
        print(f"\nTotal Calories: {total}")

    def save_data(self):
        """Save the food data to a file."""
        try:
            with open(self.data_file, "w") as f:
                json.dump(self.food_items, f)
            print("Data saved successfully.")
        except IOError:
            print("Error: Unable to save data.")

    def load_data(self):
        """Load food data from a file."""
        try:
            with open(self.data_file, "r") as f:
                self.food_items = json.load(f)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No previous data found. Starting fresh.")
        except IOError:
            print("Error: Unable to load data.")

    def delete_item(self, index):
        """
        Delete a food item by its index.
        :param index: Index of the food item (1-based).
        """
        try:
            item = self.food_items.pop(index - 1)
            print(f"Deleted: {item['name']} - {item['calories']} calories.")
        except IndexError:
            print("Error: Invalid index.")

def main():
    tracker = FoodCalorieTracker()
    while True:
        print("\n--- Food Calorie Tracker ---")
        print("1. Add Food")
        print("2. View Food Items")
        print("3. Total Calories")
        print("4. Delete Food Item")
        print("5. Save and Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            food_name = input("Enter food name: ")
            calories = input("Enter calories: ")
            tracker.add_food(food_name, calories)
        elif choice == "2":
            tracker.view_food_items()
        elif choice == "3":
            tracker.total_calories()
        elif choice == "4":
            tracker.view_food_items()
            index = input("Enter the index of the item to delete: ")
            if index.isdigit():
                tracker.delete_item(int(index))
            else:
                print("Error: Index must be a number.")
        elif choice == "5":
            tracker.save_data()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
