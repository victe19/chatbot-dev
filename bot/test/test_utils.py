import bot.src.utils.utils as utils

def test_json_parser():
    filename =  "bot/data/test.json"
    expected_dict = [
        {
            "name": "Molecule Man",
            "age": 29,
            "secretIdentity": "Dan Jukes",
            "powers": [
            "Radiation resistance",
            "Turning tiny",
            "Radiation blast"
            ]
        },
        {
            "name": "Madame Uppercut",
            "age": 39,
            "secretIdentity": "Jane Wilson",
            "powers": [
            "Million tonne punch",
            "Damage resistance",
            "Superhuman reflexes"
            ]
        }
    ]

    output_dict = utils.json_parser(filename)

    assert output_dict == expected_dict


def test_preprocess():
    query = "Hola, em dic Victor i sóc estudiant de ciències.-"
    expected_word_list = 'hola em dic victor i sóc estudiant de ciències-'

    word_list = utils.preprocess(query)
    
    assert word_list == expected_word_list


def test_query_to_list():
    query = 'hola em dic victor i sóc estudiant de ciències-'
    expected_word_list = ['hola', 'em', 'dic', 'victor', 'i', 'sóc', 'estudiant', 'de', 'ciències-']

    word_list = utils.query_to_list(query)
    
    assert word_list == expected_word_list


def test_words_to_nums():
    query = "vull picar al sisè número quatre vegades i fins que pugui ser el primer dels 3"
    expected_query = "vull picar al 6 número 4 vegades i fins que pugui ser el 1 dels 3"
    
    output_query = utils.words_to_nums(query)

    assert output_query == expected_query