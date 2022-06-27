from operator import itemgetter
import sys
import bot.src.utils.utils as utils


def greeting(query:str) -> float:
    """_summary_

    Args:
        query (str): query without processing

    Returns:
        confidence (float): probability that this query belongs to the intent greet
    """    
    query = utils.query_to_list(query)
    word_list = ["hola", "holaa", "ola", "salutacions", "hello"]

    if any(word in query for word in word_list):
        return 90

    word_list = ["bones", "bona", "bon", "buenas", "hey", "hi"]
    if any(word in query for word in word_list):
        return 75

    return 0


def cleverbot(query:str) -> float:
    """_summary_

    Args:
        query (str): query without processing

    Returns:
        confidence (float): probability that this query belongs to the intent greet
    """    
    query = utils.query_to_list(query)
    word_list = ["que saps fer", "que pots fer", "que saps", "ets intl·ligent", "que et puc demanar", "que fas", "que et puc preguntar"]

    for word in word_list:
        if " " in word:
            if all(split_words in query for split_words in word.split()):
                return 90
    
    if any(word in query for word in word_list):
        return 90

    return 0


def insults(query:str) -> float:
    """_summary_

    Args:
        query (str): query without processing

    Returns:
        confidence (float): probability that this query belongs to the intent greet
    """    
    query = utils.query_to_list(query)
    word_list = ["gilipollas", "tonto", "retrassat", "fill de puta", "cabrón", "idiota"]

    for word in word_list:
        if " " in word:
            if all(split_words in query for split_words in word.split()):
                return 90
    
    if any(word in query for word in word_list):
        return 90

    return 0


def date(query:str) -> float:
    """_summary_

    Args:
        query (str): query without processing

    Returns:
        confidence (float): probability that this query belongs to the intent greet
    """    
    query = utils.query_to_list(query)
    word_list = ["quin dia es avui", "que som avui", "dir la data", "data avui"]

    for word in word_list:
        if " " in word:
            if all(split_words in query for split_words in word.split()):
                return 90
    
    if any(word in query for word in word_list):
        return 90

    return 0


def help(query:str) -> float:
    """_summary_

    Args:
        query (str): query without processing

    Returns:
        confidence (float): probability that this query belongs to the intent greet
    """    
    query = utils.query_to_list(query)
    word_list = ["no se utilitzar", "ajuda", "no se utilitzar-te", "com t'utilitzo", "com ho faig", "com et puc utilitzar", "help", "com funciona", "com funciones"]

    for word in word_list:
        if " " in word:
            if all(split_words in query for split_words in word.split()):
                return 90
    
    if any(word in query for word in word_list):
        return 90

    return 0


def how_are_you(query:str) -> float:
    """_summary_

    Args:
        query (str): query without processing

    Returns:
        confidence (float): probability that this query belongs to the intent greet
    """    
    query = utils.query_to_list(query)
    word_list = ["com estas"]

    for word in word_list:
        if " " in word:
            if all(split_words in query for split_words in word.split()):
                return 90
    
    if any(word in query for word in word_list):
        return 90

    return 0


def confirm(query:str) -> float:
    """_summary_

    Args:
        query (str): query without processing

    Returns:
        confidence (float): probability that this query belongs to the intent confirm
    """    
    query = utils.query_to_list(query)
    word_list = ["confirmo", "d'acord", "vale", "ok", "okey", "yes"]

    if any(word in query for word in word_list):
        return 90

    word_list = ["genial", "perfecte"]
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
    word_list = ['negatiu', "noo"] 

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
    word_list = ["informacio", "informacio", "info", "dubtes", "dubte", "interessat", "informacion", "information" ]

    if any(word in query for word in word_list):
        return 90 
    
    word_list = ["saber", "know"]
    if any(word in query for word in word_list):
        return 75

    return 0


def bot(query:str) -> float:
    """_summary_

    Args:
        query (str): query without processing

    Returns:
        confidence (float): probability that this query belongs to the intent info
    """    

    query = utils.query_to_list(query)
    word_list = ["bot", "assistent", "robot"]

    
    if any(word in query for word in word_list):
        return 90 
    
    word_list = ["artificial"]
    if any(word in query for word in word_list):
        return 75

    return 0


def goodbye(query:str) -> float:
    """_summary_

    Args:
        query (str): query without processing

    Returns:
        confidence (float): probability that this query belongs to the intent greet
    """    
    query = utils.query_to_list(query)
    word_list = ["adeu", "adeu", "deu", "adios","chao", "bye"]

    if any(word in query for word in word_list):
        return 90

    word_list = ["fins un altre", "chau"]
    if any(word in query for word in word_list):
        return 75

    return 0


def operator(query:str) -> float:
    """_summary_

    Args:
        query (str): query without processing

    Returns:
        confidence (float): probability that this query belongs to the intent info
    """    

    query = utils.query_to_list(query)
    word_list = ["persona", "huma", "humano", "person"]

    if any(word in query for word in word_list):
        return 90 
    
    word_list = ["persone"]
    if any(word in query for word in word_list):
        return 75

    return 0

    
def get_module_functions() -> list:
    module_functions = dir(sys.modules[__name__])
    module_core_functions = []
    for function in module_functions:
        if '_intent_' in function:
            module_core_functions.append(eval(function))

    return module_core_functions


def intent_extraction(query: str) -> str:
    confidences = []
    intent_list = [greeting, confirm, reject, info, bot, operator, goodbye, cleverbot, insults, help, how_are_you, date]

    for intent in intent_list:
        confidence = intent(query)
        confidences.append([intent.__name__,confidence])
    
    confidences.sort(key=itemgetter(1), reverse=True)
    if confidences[0][1] != 0:
        return confidences[0]
    else: 
        return [None, 0] 
