from operator import itemgetter
import utils


def greeting(query:str) -> float:
    """_summary_

    Args:
        query (str): query without processing

    Returns:
        confidence (float): probability that this query belongs to the intent greet
    """    
    query = utils.query_to_list(query)
    word_list = ["hola", "holaa", "ola", "salutacions"]

    if any(word in query for word in word_list):
        return 90

    word_list = ["bones", "bona", "bon", "hey"]
    if any(word in query for word in word_list):
        return 75

    return 0


def confirm(query:str) -> float:
    """_summary_

    Args:
        query (str): query without processing

    Returns:
        confidence (float): probability that this query belongs to the intent confirm
    """    
    query = utils.query_to_list(query)
    word_list = ["si", "sí", "confirmo", "d'acord", "vale", "ok", "okey"]

    if any(word in query for word in word_list):
        return 90

    word_list = ["genial", "perfecte", "bé"]
    if any(word in query for word in word_list):
        return 80
    
    return 0


def reject(query:str) -> float:
    """_summary_

    Args:
        query (str): query without processing

    Returns:
        confidence (float): probability that this query belongs to the intent reject
    """    
    query = utils.query_to_list(query)    
    word_list = ['no', 'negatiu', "noo"] 

    if any(word in query for word in word_list):
        return  90

    word_list = ["tampoc"]
    if any(word in query for word in word_list):
        return 75   

    return 0


def info(query:str) -> float:
    """_summary_

    Args:
        query (str): query without processing

    Returns:
        confidence (float): probability that this query belongs to the intent info
    """    

    query = utils.query_to_list(query)
    word_list = ["informació", "informacio", "info", "dubtes", "dubte", "interessat" ]

    if any(word in query for word in word_list):
        return 90 
    
    word_list = ["saber"]
    if any(word in query for word in word_list):
        return 75

    return 0


def main_intent(query: str) -> str:
    confidences = []
    intent_list = [greeting, confirm, reject, info]

    for intent in intent_list:
        confidence = intent(query)
        confidences.append([intent.__name__,confidence])

    #TODO: ignore greeting when more intents    
    
    confidences.sort(key=itemgetter(1), reverse=True)
    if confidences[0][1] != 0:
        return confidences[0]
    else: 
        return [None] 
