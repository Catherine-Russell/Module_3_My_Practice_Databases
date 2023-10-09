# 1. Extract nouns from user stories or specifications
    As a food lover,
    So I can stay organised and decide what to cook,
    I'd like to keep a list of all my recipes with their names.

    As a food lover,
    So I can stay organised and decide what to cook,
    I'd like to keep the average cooking time (in minutes) for each recipe.

    As a food lover,
    So I can stay organised and decide what to cook,
    I'd like to give a rating to each of the recipes (from 1 to 5).

        NOUNS: recipes, names, average_cooking_time, rating

# 2. Infer Table name and columns 
    table name = recipes
    columns = names, average_cooking_time, rating

# 3. Decide column types
    id = SERIAL
    names = text
    average_cooking_time = int
    rating = int CHECK (rating >= 0 AND testing <=5)

# 4. Write SQL
    CREATE TABLE recipes (
        id SERIAL PRIMARY KEY
        names text
        average_cooking_time int
        rating int CHECK (rating >= 0 and rating <=5)
    )

# 5.
