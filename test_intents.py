import pytest

import intents

def test_preprocess():
    query = "Hola, em dic Victor i sóc estudiant de ciències.-"
    expected_word_list = ['hola', 'em', 'dic', 'victor', 'i', 'sóc', 'estudiant', 'de', 'ciències-']

    word_list = intents.preprocess(query)
    
    assert word_list == expected_word_list


def test_greeting():
    query = 'hola, em dic Victor.-'
    expected_confidence = 90

    confidence = intents.greeting(query)
    
    assert confidence == expected_confidence


def test_confirm():
    query = 'hola, em dic Victor i sí que accepto les condicions.-'
    expected_confidence = 90

    confidence = intents.confirm(query)
    
    assert confidence == expected_confidence


def test_reject():
    query = 'hola, em dic Victor i no accepto les condicions.-'
    expected_confidence = 90

    confidence = intents.reject(query)
    
    assert confidence == expected_confidence


def test_info():
    query = 'hola, em dic Victor i voldria informació sobre els graus.-'
    expected_confidence = 90

    confidence = intents.info(query)
    
    assert confidence == expected_confidence

def test_main_intent():
    query = 'hola, em dic Victor i voldria informació sobre els graus.-'
    expected_intent = ['greeting', 90]

    confidence = intents.main_intent(query)
    
    assert confidence == expected_intent