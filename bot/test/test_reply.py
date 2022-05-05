import bot.src.nlg.reply as reply
from  bot.src.context import Context

def test_generate_ask_name():
    action = "ask_name"
    context = Context()
    expected_reply = "Hola, encantat de saludar-te. Primer de tot, com em puc dirigir a tu?"

    response = reply.generate(action, context)
    
    assert response == expected_reply


def test_generate_ask_degree():
    action = "ask_degree"
    context = Context()
    expected_reply = "D'acord , em podries indicar sobre quin grau/carrera t'agraderia saber-ne més?"

    response = reply.generate(action, context)
    
    assert response == expected_reply


def test_generate_no_understand():
    action = "no_understand"
    context = Context()
    expected_reply = "Ho sento , no t'he entès. Podríes repetir?"

    response = reply.generate(action, context)
    
    assert response == expected_reply
