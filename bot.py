import logging as log

import dialogue_manager
import entities
import intents
import nlg
import utils
from context import Context


def message(query: str, context: Context)-> list:
    """
    Generate reply to response user message. 

    Args:
        query (str): user message
        context (Context): data persistence

    Returns:
        reply: (str)
    """
    print('--------------------------------------------')
    print('Starting...')
    query = utils.preprocess(query)    
    intent = intents.main_intent(query) 
    print(f'Intent captured is --> {intent}')
    entity_list = entities._entity(query)
    print(f'List of entity captured is --> {entity_list}')
    action, context = dialogue_manager.next_action(intent, entity_list, context)
    print(f'Next action will be --> {action}')
    reply = nlg.generate(action, context)
    print(f'Bot reply is --> {reply}')
    print('Response send!')
    print('--------------------------------------------')

    return reply
    