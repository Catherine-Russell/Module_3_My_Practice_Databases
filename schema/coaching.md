# 1. Extract nouns from the user stories or specification
    As a coach
    So I can get to know all students
    I want to keep a list of students' names.

    As a coach
    So I can get to know all students
    I want to assign tags to students (for example, "happy", "excited", etc).

    As a coach
    So I can get to know all students
    I want to be able to assign the same tag to many different students.

    As a coach
    So I can get to know all students
    I want to be able to assign many different tags to a student.

        NOUNS = students, names, tags

# 2. Infer the Table name and columns
    students - name
    tags - emotion
    join - student_id, tag_id

# 3. Decide the column types
    students:
        id = serial
        name varchar(255)
    tags:
        id = serial
        emotion = VARCAHR(255)
    join:
        student_id = int
        tag_id = int

# 4. Decide on tables' relationships
    many to many


# 5. Write the SQL to create a file (in SQL file)
    CREATE TABLE students (
        id SERIAL PRIMARY KEY
        name VARCHAR(255)
    );

    CREATE TABLE tags (
        id = SERIAL PRIMARY KEY
        emotion = VARCHAR(255)
    );

    CREATE TABLE students_tags (
        student_id int
        tag_id int
        CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
        CONSTRAINT fk_tag FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
    );

# 6. Create the table and link to the database (in terminal)
    
    
