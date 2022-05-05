import inspect
import re
import sys

import bot.src.utils.utils as utils

degrees_core_regex = "(?: ?(dades|(?:sistemes|electrònica) de telecomunicació|telecos|informàtica|info |química|gestió aeronàutica))" #done
degrees_regex = "(?:grau|carrera)?(?: en | de | d')?(?:enginyeria)?(?: de| en)?" + degrees_core_regex #done

course_regex = "((?:primer|segon|tercer|quart)|[1-4](?:r|n|t)?)(?: curs| any)?" #done
departaments_regex = "(departament)( de |d')?(ciències de la computació|enginyeria electrònica|arquitectura)"
subjects_regex = "(?:(?:assignatura |materia )(?:de |d')?((?:[^,.\\s]*)(?:(?: de | dels? | i | d'| |, )(?:[^,.\\s]*))?))" #50%
mentions_regex = "(?:(?:menció)(?: en | de )?(?:enginyeria del? |tecnologies de la )?(computació|software|computadors|informació))" #done
professors_regex = ""
semester_regex = "((primer|1er|1)|(segon|2n|2))(semestre|quatrimestre|període)" 
year_regex = "(?:(?:any )?(\\d{2,4}|que bé|següent)(?: any)?)" #done
username_regex = "(?:(?:soc|sóc)(?: el )?|el meu nom (?:és |es )|em dic )([^,.\\s]*)" #done

entities_dict = {
    'academic': ['expedient acadèmic', 'expedient'],
    'exams': ['exàmens', 'proves', 'parcials', 'finals', 'exàmen'],
    'exchange': ['estudiar fora', 'erasmus', 'exchange', 'sicue', 'destinacions', 'mobilitat', 'programa mobilitat'],
    'internship': ['pràctiques', 'pràcticum', 'internship', 'estades', 'empresa', 'empreses'],
    'registration': ['matrícula', 'matricular-me', 'matrícules', 'matriculació'],
    'schedule': ['horari', 'horaris', 'hores', 'franjes'],
    'calendar': ['data', 'dates', 'dia', 'dies', 'setmana', 'setmanes'],
    'teaching_guide': ['guia docent', 'guia', 'docent', 'franjes'],
    'permanence': ['règim de permanència', 'permanència'],
    'procedures': ['tràmit', 'tràmits', 'gestió acadèmica',],
    'credit_recognition': ['reconeixament de crèdits'],
    'tfg': ['final de grau', 'tfg', 'treball final'],

    }

def _entity_course(query: str) -> str:
    function_name = sys._getframe(  ).f_code.co_name.replace("_entity_","")
    query = utils.words_to_nums(query)
    m = re.search(course_regex, query)

    if m:
        query = query.replace(m.group(0), "")
        if m.group(1):
            course = m.group(1)
        return [function_name, course]
    return None


def _entity_degree(query: str) -> str:
    function_name = sys._getframe(  ).f_code.co_name.replace("_entity_","")
    m = re.search(degrees_regex, query)

    if m:
        query = query.replace(m.group(0), "")
        if m.group(1):
            degree = m.group(1)
        return [function_name, degree]
    return None


def _entity_mention(query: str) -> str:
    function_name = sys._getframe(  ).f_code.co_name.replace("_entity_","")
    m = re.search(mentions_regex, query)

    if m:
        query = query.replace(m.group(0), "")
        if m.group(1):
            mention = m.group(1)
        return [function_name, mention]
    return None


def _entity_subject(query: str) -> str:
    function_name = sys._getframe(  ).f_code.co_name.replace("_entity_","")
    m = re.search(subjects_regex, query)

    if m:
        query = query.replace(m.group(0), "")
        if m.group(1):
            subject = m.group(1)
        return [function_name, subject]
    return None


# def _entity_year(query: str) -> str:
#     function_name = sys._getframe(  ).f_code.co_name.replace("_entity_","")
#     m = re.search(year_regex, query)

#     if m:
#         query = query.replace(m.group(0), "")
#         if m.group(1):
#             year = m.group(1)
#         return [function_name, year]
#     return None


# def _entity_professor(query: str) -> str:
#     function_name = sys._getframe(  ).f_code.co_name.replace("_entity_","")
#     m = re.search(degrees_regex, query)

#     if m:
#         query = query.replace(m.group(0), "")
#         if m.group(1):
#             professor = m.group(1)
#         return [function_name, professor]
#     return None


def _entity_username(query: str) -> str:
    function_name = sys._getframe(  ).f_code.co_name.replace("_entity_","")
    m = re.search(username_regex, query)

    if m:
        query = query.replace(m.group(0), "")
        if m.group(1):
            username = m.group(1)
        return [function_name, username]
    return None


def _entity_year(query: str) -> str:
    function_name = sys._getframe(  ).f_code.co_name.replace("_entity_","")

    m = re.search(degrees_regex, query)

    if m:
        query = query.replace(m.group(0), "")
        if m.group(1):
            year = m.group(1)
        return [function_name, year]
    return None


def _entity(query: str) -> list:
    entities_found = []
    query = utils.preprocess(query)    
    query = utils.query_to_list(query)

    for entity in entities_dict:
        if any(word in query for word in entities_dict[entity]):
            entities_found.append([entity, True])  


    return entities_found #TODO: sorted list
    

def get_module_functions() -> list:
    module_functions = dir(sys.modules[__name__])
    module_core_functions = []
    for function in module_functions:
        if '_entity_' in function:
            module_core_functions.append(eval(function))

    return module_core_functions


def entities_extraction(query: str) -> list:
    function_list = get_module_functions()
    entities_list = _entity(query)

    for function in function_list:
        entity = function(query)
        if entity != None:
            entities_list.append(entity)
    
    return entities_list #TODO: sorted list






