from bot.src.context import Context
import bot.src.flowbot as bot

def test_message_1():
    query = "hola em dic George"
    context = Context()
    expected_reply = "Hola george, encantat de saludar-te. Sóc en G.A.V.I.À el teu assistent virtual"
    reply = bot.message(query, context)

    assert reply == expected_reply

def test_message_2():
    query = "Em dic Victor i m'agradaria obtenir informació sobre la guia docent del l'assignatura de TFG"
    context = Context()
    expected_reply = "Mira victor, en aquest enllaç podràs trobar la guia docent que em demanes"

    reply = bot.message(query, context)

    assert reply == expected_reply


def test_message_3():
    query = "em dic víctor i m'agraderia saber quina és la guía docent del tfg ja que el curso aquest any"
    context = Context()
    expected_reply = "Mira víctor, en aquest enllaç podràs trobar la guia docent que em demanes"

    reply = bot.message(query, context)

    assert reply == expected_reply


def test_message_4():
    query = "M'agraderia saber quina és la guía docent del tfg ja que el curso aquest any"
    context = Context()
    expected_reply = "Mira , en aquest enllaç podràs trobar la guia docent que em demanes"

    reply = bot.message(query, context)

    assert reply == expected_reply
