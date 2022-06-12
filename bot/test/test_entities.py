import pytest
import bot.src.nlu.entities as entities

def test_entity_course():
    test_query = [
        ("voldria informació sobre el primer any del grau d'enginyeria informàtica", ["course", "1"]),
        ("voldria informació sobre el 2n any del grau en d'enginyeria informàtica", ["course", "2n"]),
        ("voldria informació sobre el 3r any del grau d'enginyeria informàtica", ["course", "3r"]),
        ("voldria informació sobre el quart any del grau d'enginyeria informàtica", ["course", "4"]),        
    ]

    for test in test_query:
        query, expected_entity = test
        entity = entities._entity_course(query)

        assert entity == expected_entity


def test_entity_degree():
    test_query = [
        ("voldria informació sobre el primer any del grau d'enginyeria informàtica", ["degree", "informàtica"]),
        ("voldria informació sobre el primer any del grau en enginyeria de dades", ["degree", "dades"]),
        ("grau de gestió aeronàutica", ["degree", "gestió aeronàutica"]),
        ("voldria informació sobre el primer any del grau d'informàtica", ["degree", "informàtica"]),
        ("voldria informació sobre el primer any del grau enginyeria química", ["degree", "química"]),
        ("voldria informació sobre el primer any del grau de enginyeria en electrònica de telecomunicació", ["degree", "electrònica de telecomunicació"]),
        ("voldria informació sobre el primer any del grau d'enginyeria en sistemes de telecomunicació", ["degree", "sistemes de telecomunicació"]),
        ("què és el grau d'informàtica", ["degree", "informàtica"]),
        ("puc fer la carrera d'informàtica", ["degree", "informàtica"]),
        ("enginyeria química", ["degree", "química"]),
    ]

    for test in test_query:
        query, expected_entity = test
        entity = entities._entity_degree(query)

        assert entity == expected_entity


def test_entity_mention():
    test_query = [
        ("menció en computació", ["mention", "computació"]),
        ("menció en enginyeria del software i quines assignatures té", ["mention", "software"]),
        ("a l'escola és cursa la menció en enginyeria de computadors", ["mention", "computadors"]),
        ("menció en tecnologies de la informació", ["mention", "informació"]),
        ("menció en enginyeria del software i quines assignatures té", ["mention", "software"]),
        ("a l'escola és cursa la menció en enginyeria de computadors", ["mention", "computadors"]),
        ("menció en tecnologies de la informació", ["mention", "informació"]),
        # ("teconologies de la informació", ["mention", "informació"]),
        # ("computació", ["mention", "computació"]),
        # ("software", ["mention", "software"]),
        ("menció de computació", ['mention', 'computació']),
        ("menció en inteligència artificial", None),
        ("menció en", None),
    ]

    for test in test_query:
        query, expected_entity = test
        entity = entities._entity_mention(query)

        assert entity == expected_entity

def test_entity_username():
    test_query = [
        ("hola el meu nom es àlex", ["username", "àlex"]),
        ("sóc el victor, tú qui ets", ["username", "victor"]),
        ("encantat de conèixet, em dic víctor", ["username", "víctor"]),
        ("el meu nom es victor", ["username", "victor"]),
        ("hola soc el victor", ["username", "victor"]),
    ]

    for test in test_query:
        query, expected_entity = test
        entity = entities._entity_username(query)

        assert entity == expected_entity


def test_entity_year():
    test_query = [
        ("començo les pràctiques l'any que ve", ["year", "2023"]),
        ("l'any que ve vull fer química", ["year", "2023"]),
        ("l'any següent m'agraderia fer un master", ["year", "2023"]),
        ("començo les pràctiques l'any que ve", ["year", "2023"]),
        # ("l'any 22 ve vull fer química", ["year", "2022"]),
        ("l'any 2022 m'agraderia fer un master", ["year", "2022"]),
        ("m'agraderia anar a Mallorca aquest any  i tal", ["year", "2022"]),
        # ("vull un any mes de contracte", ["year", ""]),
    ]

    for test in test_query:
        query, expected_entity = test
        entity = entities._entity_year(query)

        assert entity == expected_entity


def test_entity():
    test_query = [
        ("voldria informació sobre els horaris de primer any del grau d'enginyeria informàtica", [["schedule", True]]),
        ("voldria informació sobre la matrícula del primer any del grau en enginyeria de dades", [["registration", True]]),
        ("voldria informació sobre la matrícula del primer any del grau en enginyeria de dades i els horaris", [["registration", True], ["schedule", True]]),
        ("com funciona la matriculació del tfg i quins són els seus horaris sobre la matrícula del primer any del grau en enginyeria de dades i els horaris", [["registration", True],  ["schedule", True], ["tfg", True]]),
    ]

    for test in test_query:
        query, expected_entity = test
        entity = entities._entity(query)

        assert entity == expected_entity
        
        
@pytest.mark.skip(reason="no way of currently testing this")
def test_get_function_name():
    function_names = entities.get_module_functions()
    expected_functionnames = [
        '_entity_course', 
        '_entity_degree', 
        '_entity_department', 
        '_entity_mencion',           
        '_entity_professor', 
        '_entity_semester', 
        '_entity_username', 
        '_entity_year'
    ]
    
    assert function_names == expected_functionnames


def test_entities_extraction():
    test_query = [
        ("voldria informació sobre els horaris de primer del grau d'enginyeria informàtica", [["schedule", True], ["course", "1"], ["degree", "informàtica"]]),
        ("voldria informació sobre els horaris de segon", [["schedule", True], ["course", "2"]]),
        ("voldria informació sobre el tfg d'enginyeria química", [["tfg", True], ["degree", "química"]]),
        ("hola em dic víctor i voldria informació", [["username", "víctor"]])
    ]

    for test in test_query:
        query, expected_entity = test
        entity = entities.entities_extraction(query)

        assert entity == expected_entity


def test__sub_entity():
    test_query = [
        ("voldria informació sobre la durada del tfg", [["tfg_duration", True]]),
        ("voldria informació sobre la durada del partit de futbol", [[""]]),
    ]

    for test in test_query:
        query, expected_subentity = test
        subentity = entities._sub_entity(query, 'tfg')

        assert subentity == expected_subentity