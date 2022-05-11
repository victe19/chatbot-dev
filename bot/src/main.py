from colorama import Fore, Style

import bot.src.flowbot as bot
from context import Context
from api.main import get_messages_from_conversation, post_messages_to_conversation


context = Context()

# login()
query = get_messages_from_conversation()
while 1:
    while query == None:
        query = get_messages_from_conversation()
    print(f"{Fore.GREEN}User:{Fore.WHITE} {query}")
    reply = bot.message(query, context)
    query = None
    print(f"{Fore.YELLOW}Bot:{Fore.WHITE} {reply}")
    post_messages_to_conversation(reply)
    while query == None:
        query = get_messages_from_conversation()



