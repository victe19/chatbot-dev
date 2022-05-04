import src.dialogue_manager as dialogue_manager
import src.nlg.reply as reply
import src.nlu.entities as entities
import src.nlu.intents as intents
import src.utils.utils as utils
from src.context import Context


def message(query: str, context: Context())-> list:
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
    intent = intents.intent_extraction(query) 
    print(f'Intent captured is --> {intent}')
    entity_list = entities.entities_extraction(query)
    print(f'List of entity captured is --> {entity_list}')
    action, context = dialogue_manager.next_action(intent, entity_list, context)
    print(f'Context until now--> {context}')
    print(f'Next action will be --> {action}')
    response = reply.generate(action, context)
    print(f'Bot reply is --> {response}')
    print('Response send!')
    print('--------------------------------------------')

    return response
    