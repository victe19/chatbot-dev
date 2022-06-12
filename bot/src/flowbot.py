import bot.src.dialogue_manager as dialogue_manager
import bot.src.nlg.reply as reply
import bot.src.nlu.entities as entities
import bot.src.nlu.intents as intents
import bot.src.utils.utils as utils
from bot.src.context import Context


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
    print(f'Query --> {query}')
    query = utils.preprocess(query)    
    intent = intents.intent_extraction(query) 
    print(f'Intent captured is --> {intent}')
    entity_list, subentity_list = entities.entities_extraction(query)
    print(f'List of entity captured is --> {entity_list}')
    print(f'List of sub_entity captured is --> {subentity_list}')
    action, context = dialogue_manager.next_action(intent, entity_list, subentity_list, context)
    print(f'Context until now--> \n{context}')
    print(f'Next action will be --> {action}')
    # try:
    response = reply.generate(action, context)
    # except Exception as e:
    #     response = "No he trobat el que em demanes!"
    print(f'Bot reply is --> {response}')
    print('Response send!')
    print('--------------------------------------------')

    return response
    