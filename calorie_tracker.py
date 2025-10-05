#Daily Calorie Tracker CLI
#Name:Sukhvinder Kaur
#Date:04-10-2025
#Project:Mini Project

print("Welcome to the Daily Calorie Tracker CLI")
meals = []
num_meals = int(input("How many meals did you have today? "))

for i in range(1, num_meals + 1):
    meal_name = input(f"Enter name of meal {i}: ")
    calories = int(input(f"Enter calories for {meal_name}: "))
    meals.append({"name": meal_name, "calories": calories})

#calculations
total_calories = sum(meal["calories"] for meal in meals)

# Summary
print("\nToday's Meals:")
for meal in meals:
    print(f"{meal['name']} - {meal['calories']} cal")

print(f"\nTotal Calories: {total_calories}")

# Average calories per meal
if meals:
    avg_calories = total_calories / len(meals)
    print(f"Average Calories per meal: {avg_calories:.2f}")

# Warning system
calorie_limit = 2000
if total_calories > calorie_limit:
    print("\n Warning: You have exceeded your daily recommended calorie intake!")
elif total_calories < 1200:
    print("\n Warning: You have consumed very few calories today!")
else:
    print("\n Your calorie intake is within the healthy range.")

#Output table
print("\nToday's Meals:")
print("Meal Name\tCalories")
print("------------------------")
for meal in meals:
    print(f"{meal['name']}\t{meal['calories']}")


from datetime import datetime

save = input("Do you want to save this session report to a file? (yes/no): ").lower()

if save == "yes":
    filename = "A.txt"
    with open(filename, "w") as file:
        file.write(f"Session Timestamp: {datetime.now()}\n\n")
        file.write("Today's Meals:\n")
        file.write("Meal Name\tCalories\n")
        file.write("------------------------\n")
        for meal in meals:
            file.write(f"{meal['name']}\t{meal['calories']}\n")
        file.write(f"\nTotal Calories: {total_calories}\n")
        file.write(f"Average Calories per meal: {avg_calories:.2f}\n")
        if total_calories > 2000:
            file.write("Warning: You have exceeded your daily recommended calorie intake!\n")
        elif total_calories < 1200:
            file.write("Warning: You have consumed very few calories today!\n")
        else:
            file.write("Your calorie intake is within the healthy range.\n")
    print(f"Session report saved successfully to '{filename}'")
    