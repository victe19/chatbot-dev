from colorama import Fore, Style

import bot.src.flowbot as bot
from context import Context
from api.main import Chatwoot_api


context = Context()

query = Chatwoot_api().get_messages_from_conversation()
while 1:
    while query == None:
        query = Chatwoot_api().get_messages_from_conversation()
    # query = pritnf"{Fore.GREEN}User:{Fore.WHITE} ")
    # print(response)
    reply = bot.message(query, context)
    query = None
    print(f"{Fore.YELLOW}Bot:{Fore.WHITE} {reply}")
    Chatwoot_api().post_messages_to_conversation(reply)
    while query == None:
        query = Chatwoot_api().get_messages_from_conversation()



