import pytest

import entities

def test_extract_course():
    test_query = [
        ("voldria informació sobre el primer any del grau d'enginyeria informàtica", "1"),
        ("voldria informació sobre el 2n any del grau en d'enginyeria informàtica", "2n"),
        ("voldria informació sobre el 3r any del grau d'enginyeria informàtica", "3r"),
        ("voldria informació sobre el quart any del grau d'enginyeria informàtica", "4"),        
    ]

    for test in test_query:
        query, expected_entity = test
        entity = entities.extract_entity_course(query)

        assert entity == expected_entity


def test_extract_degree():
    test_query = [
        ("voldria informació sobre el primer any del grau d'enginyeria informàtica", "informàtica"),
        ("voldria informació sobre el primer any del grau en enginyeria de dades", "dades"),
        ("grau de gestió aeronàutica", "gestió aeronàutica"),
        ("voldria informació sobre el primer any del grau d'informàtica", "informàtica"),
        ("voldria informació sobre el primer any del grau enginyeria química", "química"),
        ("voldria informació sobre el primer any del grau de enginyeria en electrònica de telecomunicació", "electrònica de telecomunicació"),
        ("voldria informació sobre el primer any del grau d'enginyeria en sistemes de telecomunicació", "sistemes de telecomunicació"),
        ("què és el grau d'informàtica", "informàtica"),
        ("puc fer la carrera d'informàtica", "informàtica"),
    ]

    for test in test_query:
        query, expected_entity = test
        entity = entities.extract_entity_degree(query)

        assert entity == expected_entity

