from cmath import e
from typing import List
from colorama import Fore


import bot.src.flowbot as bot
from context import Context
import api.main as api
import threading
import logging
import time

print("Loading chat server")

context = Context()

def init_conversation(conversation_id: str):
    query = api.get_messages_from_conversation(conversation_id)
    while context.adeu == False:
        # start = time.clock() 
        while query == None: #or elapsed >= 20:
            # elapsed = time.clock()
            # elapsed = elapsed - start
            query = api.get_messages_from_conversation(conversation_id)
            time.sleep(2)

        # print(f"{Fore.GREEN}User:{Fore.WHITE} {query}")
        reply = bot.message(query, context)
        query = None
        # print(f"{Fore.YELLOW}Bot:{Fore.WHITE} {reply}")
        api.post_messages_to_conversation(reply, conversation_id)
    
    # api.post_messages_to_conversation("Conversa tancada.", conversation_id)
    # api.post_exit_status(conversation_id)
    # print(f'Estic activo amb el context {context.adeu}')



def substract_lists(list_1: List, list_2: List):
    return [el for el in list_1 if el not in list_2 ]

# # login()

def starter():
    print("Starting chat server")
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    conversations_slack = []
    threads = []

    num_retries = 0
    while 1:
        try:
            conversations = api.get_all_conversations()
            print(f"conversations --> {conversations}")
        except Exception as e:
            num_retries += 1
            if num_retries > 5:
                break
            continue
        if len(conversations) != len(conversations_slack):
            conversations_to_solve = substract_lists(conversations, conversations_slack)
            print(f"Conversation_slack --> {conversations_slack}")
            print(f"Conversation to solve --> {conversations_to_solve}")
            conversations_slack = conversations
            for conversation in conversations_to_solve:
                logging.info("Main    : create and start thread %d.", conversation)
                t = threading.Thread(target=init_conversation, args=(conversation,))
                threads.append(t)
                t.start()        
            conversations_to_solve = []
        time.sleep(2)


if __name__ == "__main__":
    starter()
        
            

        # for conversation, thread in enumerate(threads):
        #     logging.info("Main    : before joining thread %d.", conversation)
        #     thread.join()
        #     logging.info("Main    : thread %d done", conversation)