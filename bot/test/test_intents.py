import src.nlu.intents as intents


def test_greeting():
    query = 'hola em dic Victor.-'
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
    test_query = [
            ('hola, em dic Victor i voldria informació sobre els graus.-', ['info', 90]),
            ('em dic Victor i si que accepto les condicions.-', ['confirm', 90]),
            ('em dic Victor i no accepto les condicions.-', ['reject', 90]),
            ('em dic Victor i voldria informació sobre els graus.-', ['info', 90]),
            ('vull conèixer enginyeria química', [None, 0]),          
        ]   

    for test in test_query:
        query, expected_intent = test
        confidence = intents.intent_extraction(query)
        assert confidence == expected_intent