import bot.src.dialogue_manager as dialogue_manager
import bot.src.nlg.reply as reply
import bot.src.nlu.entities as entities
import bot.src.nlu.intents as intents
import bot.src.utils.utils as utils
from bot.src.context import Context
from colorama import Fore



def message(query: str, context: Context())-> list:
    """
    Generate reply to response user message. 

    Args:
        query (str): user message
        context (Context): data persistence

    Returns:
        reply: (str)
    """
    print('----------------------------------------------------------------------------')
    print('Starting...')
    print(f"{Fore.RED}Starting...{Fore.WHITE}")
    print(f"{Fore.CYAN}Query --> {Fore.WHITE} {query}")
    query = utils.preprocess(query)    
    intent = intents.intent_extraction(query) 
    print(f"{Fore.CYAN}Intent captured is --> {Fore.WHITE} {intent}")
    entity_list, subentity_list = entities.entities_extraction(query, context.language)
    print(f"{Fore.CYAN}List of entity captured is --> {Fore.WHITE} {entity_list}")
    print(f"{Fore.CYAN}List of sub_entity captured is --> {Fore.WHITE} {subentity_list}")
    action, context = dialogue_manager.next_action(intent, entity_list, subentity_list, context)
    print(f"{Fore.CYAN}Context until now-->\n{Fore.WHITE}{context}")
    print(f"{Fore.CYAN}Next action will be --> {Fore.WHITE} {action}")
    # response = reply.generate(action, context)
    try:
        response = reply.generate(action, context)
    except Exception as e:
        response = "No he trobat el que em demanes. M'ho pots tornar a demanar?"
    print(f"{Fore.CYAN}Bot reply is --> {Fore.WHITE} {response}")
    print(f"{Fore.RED}Response send! {Fore.WHITE}")
    print('----------------------------------------------------------------------------')

    return response
    