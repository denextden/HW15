query_1 = """
    CREATE TABLE colors ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        color VARCHAR(50) 
    )
    """

query_2 = """
    CREATE TABLE breeds ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        breed VARCHAR(50) 
    ) 
    """

query_3 = """
    CREATE TABLE animal_type (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        animal_type VARCHAR(50)
    )
    """



query_4 = """ 
    CREATE TABLE new_animals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        animal_id VARCHAR(50),
        animal_type_id INTEGER,
        'name' VARCHAR(50),
        breed_id INTEGER,
        color_1_id INTEGER,
        color_2_id INTEGER,
        date_of_birth DATETIME,  
        FOREIGN KEY(animal_type_id) REFERENCES animal_type(id),
        FOREIGN KEY(breed_id) REFERENCES breeds(id),
        FOREIGN KEY(color_1_id) REFERENCES colors(id),
        FOREIGN KEY(color_2_id) REFERENCES colors(id)
    )   
    """


query_5 = """ 
    CREATE TABLE outcome (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        animal_id INTEGER, subtype VARCHAR(50),
        `type` VARCHAR(50), 
        'month' INTEGER, 
        'year' INTEGER, 
        age_upon_outcome VARCHAR(50),
        new_animals_id INTEGER,
        FOREIGN KEY(animal_id) REFERENCES new_animals(id), 
        FOREIGN KEY(new_animals_id) REFERENCES new_animals(id)
    ) 
    """

query_6 = """ 
    INSERT INTO colors (color)
        SELECT DISTINCT trim(color1) FROM animals
        UNION ALL
        SELECT DISTINCT trim(color2) FROM animals 
    """

query_7 = """
    INSERT INTO breeds (breed)
        SELECT DISTINCT breed FROM animals
    """

query_8 = """ 
    INSERT INTO animal_type (animal_type)
        SELECT DISTINCT animal_type FROM animals 
    """


query_9 = """
    INSERT INTO outcome (animal_id, subtype, "type", "month", 'year', age_upon_outcome)
        SELECT animal_id, outcome_subtype, outcome_type, outcome_month, outcome_year, age_upon_outcome 
        FROM animals 
    """

query_10 = """
    INSERT INTO new_animals (animal_id, animal_type_id, 'name', breed_id, color_1_id, date_of_birth)
        SELECT DISTINCT animals.animal_id, animal_type.id, animals.name, breeds.id AS breed, animals.color1, animals.date_of_birth
    FROM animals
    JOIN colors
        ON colors.color = animals.color1
    LEFT JOIN breeds
        ON animals.breed = breeds.breed
    LEFT JOIN animal_type
        ON animals.animal_type = animal_type.animal_type
        
    """

# query_11 = """
#     INSERT INTO new_animals (animal_type_id)
#         SELECT DISTINCT animal_type.id
#         FROM animal_type
#         JOIN animals ON animals.animal_type = animal_type.animal_type
#         WHERE animals.animal_id = new_animals.animal_id
#     """
#
# query_12 = """
#     INSERT INTO new_animals (breed_id)
#         SELECT DISTINCT breeds.id
#         FROM breeds
#         JOIN animals ON animals.breed = breeds.breed
#         WHERE animals.animal_id = new_animals.animal_id
#     """
# query_13 = """
#     INSERT INTO new_animals (color_1_id)
#         SELECT color
#         FROM colors
#      """
# query_14 = """
#     INSERT INTO new_animals (color_2_id)
#         SELECT DISTINCT colors.id
#         FROM colors
#         JOIN animals ON trim(animals.color2) = colors.color
#         WHERE animals.animal_id = new_animals.animal_id
#     """
