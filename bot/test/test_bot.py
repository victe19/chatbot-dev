import src.bot as bot
from src.context import Context

def test_message():
    query = "hola em dic victor"
    context = Context()
    expected_reply = 'Hola, victor, encantat de saludar-te. Com et puc ajudar?'

    reply = bot.message(query, context)

    assert reply == expected_reply

# def test_message_1():
#     query = "M'agradaria obtenir informació sobre la guia docent del l'assignatura de TFG"
#     context = Context()
#     expected_reply = "Mira, Victor, en aquest enllaç podràs trobar la guia docent que em demanes"

#     reply = bot.message(query, context)

#     assert reply == expected_reply

# def test_message1():
#     query = "vull saber informació sobre la carrera universitària"
#     context = Context()
#     expected_reply = 'ask_degree'

#     reply = bot.message(query, context)

#     assert reply == expected_reply


# def test_message2():
#     query = "em dic víctor i m'agraderia saber quina és la guía docent del tfg ja que el curso aquest any"
#     context = Context()
#     expected_reply = 'tfg_teaching_guide'

#     reply = bot.message(query, context)

#     assert reply == expected_reply


# def test_message3():
#     query = "enginyeria química"
#     context = Context()
#     expected_reply = 'ask_course'

#     reply = bot.message(query, context)

#     assert reply == expected_reply
