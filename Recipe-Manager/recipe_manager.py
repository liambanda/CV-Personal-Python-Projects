
#creates an empty list for storing recipes
recipes = []

meal_plan = {"Monday": "",
             "Tuesday": "",
             "Wednesday": "",
             "Thursday": "",
             "Friday": "",
             "Saturday": "",
             "Sunday": ""
             }
# dictionary used to store meals for each day of the day of the week

def load_recipes():

#function or reusable block of code to load recipes from files
    try:
        file = open("recipes.csv","r")
# 'r' opens file in read mode
        for line in file:
# loops each line in the file
            data = line.strip().split(",")
            if len(data) == 3:
                recipes.append(data)
        file.close()
    except:
        pass

#save recipes to file
def save_recipes():
    file = open("recipes.csv","w")
    for r in recipes:
        file.write(r[0] + "," + r[1] + "," + r[2] + "\n")
    file.close()
#ADD recipes
def add_recipes():
    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients (separate with ;) : ")
    steps = input("Enter steps (separate with ;) : ")
    recipes.append([name, ingredients, steps])
    save_recipes()
    print("Recipe added.")

def search_recipes():
    search = input("Enter recipe name: ")
    found = False
    for r in recipes:
        if r[0].lower() == search.lower():
         # compares names (case sensitive)
            print("\nName:", r[0])
            print("Ingredients:", r[1])
            print("Steps:", r[2])
        # displays matching recipes
            found = True

    if not found:
        print("Recipe not found")
        #informs user there isn't exiting recipe




# Plan which days meals are to be eaten
def plan_meals():
    print("\n---Meal Planner ---")
    #show available recipes
    print("\nAvailable recipes:")
    for r in recipes:
        print("-", r[0])

    day = input("\nEnter day of the week: ").capitalize()
    recipe_name = input("Enter recipe name: ")
    if day not in meal_plan:
        print("Invalid day")
        return
    #user inputs recipe to assign
    found = False
    for r in recipes:
        if r[0].lower() == recipe_name.lower():
            meal_plan[day] = r[0]
            found = True
            print("Meal added to", day)
    if not found:
        print("Recipe doesn't exist")

#view Meal Plan according to days
def view_meal_plan():
    print("\n--- Weekly Meal Plan ---")
    for day in meal_plan:
        if meal_plan[day] == "":
            print(day,":There is no meal planned for this day.")
        else:
            print(day + ":", meal_plan[day])


#Save meal plan to file
def save_meal_plan():
    file = open("meal_plan.txt", "w")
    for day in meal_plan:
        file.write(day + " " + meal_plan[day] + "\n")
    file.close()
# load meal plan
def load_meal_plan():
    try:
        file = open("meal_plan.txt", "r")
        for line in file:
            data = line.strip().split(",")
            if len(data) == 2:
                meal_plan[data[0]] = data[1]

        file.close()
    except:
        pass



# Shopping List, must look at meal plan, Find ingredients used, Extract all the ingredients Combine them into a list.
def generate_shopping_list():
    shopping_list = []
    for day in meal_plan:
        recipe_name = meal_plan[day]

        if recipe_name != "":
            for r in recipes:
                if r[0] == recipe_name:
                    ingredients = r[1].split(";")
                    for item in ingredients:
# to ensure there are no duplicates this line makes everything lower case e.g ("Salt") vs ("salt").
                        item = item.strip().lower()
                        if item not in shopping_list:
                            shopping_list.append(item)
    print("\n---Shopping list---")
    if len(shopping_list) == 0:
        print("No items found")
    else:
        for item in shopping_list:
            print("-", item)


# saves shopping list
def save_shopping_list():
    file = open("shopping_list.txt", "w")
    shopping_list = []
    for day in meal_plan:
        recipe_name = meal_plan[day]
        if recipe_name != "":
            for r in recipes:
                if r[0] == recipe_name:
                    ingredients = r[1].split(";")
                    for item in ingredients:
                        item = item.strip().lower()
                        if item not in shopping_list:
                            shopping_list.append(item)

    for item in shopping_list:
        file.write(item + "\n")
    file.close()
#Main program
load_recipes()
load_meal_plan()
# loads the two saved files and recipes at the start
while True:
    #infite loop for main menu
    print("Welcome to Recipe Manager")
    print("\n1 Add Recipe")
    print("2 Search Recipes")
    print("3 Plan Meals")
    print("4 View Meal Plan")
    print("5 Generate Shopping List")
    print("6 Exit Shopping List")
    choice = input("Enter choice: ")
    if choice == "1":
        add_recipes()
        save_recipes()
    elif choice == "2":
        search_recipes()

    elif choice == "3":
        plan_meals()
        save_meal_plan()
    elif choice == "4":
        view_meal_plan()
    elif choice == "5":
        generate_shopping_list()
        save_shopping_list()


