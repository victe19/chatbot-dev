from colorama import Fore, Style

import bot.src.flowbot as bot
from context import Context
from api.main import get_messages_from_conversation, post_messages_to_conversation, get_list_all_inboxes
import threading


context = Context()

def conversation_thread(inbox: str):
    """funcion que realiza el trabajo en el thread"""
    print(f"Aquesta és la conversa {inbox}")
    query = get_messages_from_conversation(inbox)
    while 1:
        while query == None:
            query = get_messages_from_conversation(inbox)
        print(f"{Fore.GREEN}User:{Fore.WHITE} {query}")
        reply = bot.message(query, context)
        query = None
        print(f"{Fore.YELLOW}Bot:{Fore.WHITE} {reply}")
        post_messages_to_conversation(reply, inbox)
        while query == None:
            query = get_messages_from_conversation(inbox)
    return

# login()
inboxes = get_list_all_inboxes()
print(f"Llista conversations: {inboxes}")
threads = list()
for inbox in inboxes:
    t = threading.Thread(target=conversation_thread, args=(inbox,))
    threads.append(t)
    t.start()

