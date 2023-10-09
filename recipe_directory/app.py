from lib.database_connection import DatabaseConnection
from lib.recipe_repository import RecipeRepository

# connect to database
connection = DatabaseConnection()
connection.connect()

# seed database
connection.seed("seeds/recipes.sql")

recipe_repo = RecipeRepository(connection)
recipes = recipe_repo.all()

for item in recipes:
    print(item)


chosen_one = recipe_repo.find(2)
print(f"Today we will eat: {chosen_one}")
