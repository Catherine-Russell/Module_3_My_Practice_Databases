# 1. Extract nouns from user stories
    As a coach
    So I can get to know all students
    I want to see a list of students' names.

    As a coach
    So I can get to know all students
    I want to see a list of cohorts' names.

    As a coach
    So I can get to know all students
    I want to see a list of cohorts' starting dates.

    As a coach
    So I can get to know all students
    I want to see a list of students' cohorts.

        NOUNS = students, students names, cohorts names, cohort starting dates, 


# 2. Infer table names and columns
    table 1 = cohorts
        columns = cohort_name, starting_date
    
    table 2 = students
        columns = names, cohorts
    
    

# 3. decide column types
    Table 1: cohorts
        id SERIAL PRIMARY KEY
        name text
        starting_date date
    
    Table 2:
        id SERIAL PRIMARY KEY
        name text
        cohort id link to cohort

# 4. Decide on tables' relationships
    Can one cohort have many students? (Yes)
    Can one student have many cohorts? (No)

    a cohort has many students
    And on the other side, a student belongs to a cohort
    In that case, the foreign key is in the table students
    
# 5. Write the SQL

# 6. Create the tables
