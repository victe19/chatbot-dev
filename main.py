from doctest import REPORT_ONLY_FIRST_FAILURE
import bot
from context import Context

while 1:
    query = input("User: ")
    context = Context()
    reply = bot.message(query, context)
    print(f"Bot: {reply}")