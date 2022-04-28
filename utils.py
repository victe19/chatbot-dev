
from posixpath import split


def words_to_nums(query: str) -> str:
    replacements = [
        ('primer', 1),
        ('segon', 2),
        ('tercer', 3),
        ('quart', 4),
        ('cinquè', 5),
        ('sisè', 6),
        ('setè', 7),
        ('vuitè', 8),
        ('novè', 9),
        ('desè', 10),

        ('un', 1),
        ('una', 1),
        ('dos', 2),
        ('dues', 2),
        ('tres', 3),
        ('quatre', 4),
        ('cinc', 5),
        ('sis', 6),       
        ('set', 7),
        ('vuit', 8),
        ('nou', 9),
        ('deu', 10),
    ]

    words_query = query.split()
    for replacement in replacements:
        if replacement[0] in words_query:
            query=query.replace(replacement[0], str(replacement[1]))
    
    return query