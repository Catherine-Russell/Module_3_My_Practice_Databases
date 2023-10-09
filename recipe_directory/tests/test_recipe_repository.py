from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

def test_get_all_records(db_connection):
    db_connection.seed('seeds/recipes.sql')
    repository = RecipeRepository(db_connection)
    assert repository.all() == [
        Recipe(1, 'Miso Ramen', 45, 5),
        Recipe(2, 'lasagne', 90, 4),
        Recipe(3, 'Tomato soup', 30, 4),
        Recipe(4, 'Omrice', 40, 1),
        Recipe(5, 'omlette', 10, 2),
        ]
    
def test_find_one_record(db_connection):
    db_connection.seed('seeds/recipes.sql')
    repository = RecipeRepository(db_connection)
    result = repository.find(3)
    assert result == Recipe(3, 'Tomato soup', 30, 4)