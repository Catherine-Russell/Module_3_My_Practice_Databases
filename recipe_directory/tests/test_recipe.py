from lib.recipe import Recipe
import pytest

def test_recipe_constructs_properly():
    recipe = Recipe(1, 'beans on toast', 5, 3)
    assert recipe.id == 1
    assert recipe.dish == 'beans on toast'
    assert recipe.average_cooking_time == 5
    assert recipe.rating == 3

    """
    test:
    - rating myst be withing 0-5
    - repr
    - eq
    """

def test_rating_must_be_above_0():
    with pytest.raises(Exception) as e:
        recipe = Recipe(1, 'beans on toast', 5, -7)
    err_msg = str(e.value)
    assert err_msg == "rating must be between 0 and 5"

def test_rating_must_be_below_5():
    with pytest.raises(Exception) as e:
        recipe = Recipe(1, 'beans on toast', 5, 6)
    err_msg = str(e.value)
    assert err_msg == "rating must be between 0 and 5"

def test_recipe_instances_formatted_beautifully():
    recipe = Recipe(1, 'beans on toast', 5, 3)
    assert str(recipe) == "Recipe(1, beans on toast, 5, 3)"

def test_instances_with_same_contents_are_the_same():
    recipe1 = Recipe(1, 'beans on toast', 5, 3)
    recipe2 = Recipe(1, 'beans on toast', 5, 3)
    assert recipe1 == recipe2