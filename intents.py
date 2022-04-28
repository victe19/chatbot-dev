from operator import itemgetter


def preprocess(query: str) -> list:
    """
    First of all the function:
        1. remove marks 
        2. remove uppercases
        3. separate each word to build a list

    Args:
        query (str): query to preprocess

    Returns:
        list: list of words splited without puntuation marks
    """

    query=query.replace(',', '').replace('.', '').lower()
    word_list = query.split()

    return word_list


def greeting(query:str) -> float:
    """_summary_

    Args:
        query (str): query without processing

    Returns:
        confidence (float): probability that this query belongs to the intent greet
    """    
    query = preprocess(query)
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
    query = preprocess(query)
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
    query = preprocess(query)    
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

    query = preprocess(query)
    word_list = ["informació", "informacio", "info"]

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
    
    confidences.sort(key=itemgetter(1), reverse=True)
    return confidences[0]
