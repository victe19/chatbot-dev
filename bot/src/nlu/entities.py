import inspect
import re
import sys
from datetime import date
import bot.src.utils.utils as utils

degree_core_regex = "(?: ?(dades|(?:sistemes|electronica) de telecomunicacio|telecos|informatica|info |quimica|gestio aeronautica))" #done
degree_regex = "(?:grau|carrera)?(?: en | de | d')?(?:enginyeria)?(?: de| en)?" + degree_core_regex #done
course_regex = "((?:primer|segon|tercer|quart)|[1-4](?:r|n|t)?)(?: curs| any)" #done
departaments_regex = "(departament)( de |d')?(ciencies de la computacio|enginyeria electronica|arquitectura)"
subject_regexx = "(?:(?:assignatura |materia )(?:de |d')?((?:[^,.\\s]*)(?:(?: de | dels? | i | d'| |, )(?:[^,.\\s]*))?))" #50%
subject_regex = "(algebra|calcul|electricitat i electronica|fonaments dels computadors|fonaments d'informatica|matematica discreta|metodologia de la programacio|organitzacio i gestio d'empreses|fonaments d'enginyeria|estadistica|arquitectura de computadors|bases de dades|enginyeria del software|estructura de computadors|informacio i seguretat|intel·ligencia artificial|laboratori de programacio|sistemes operatius|xarxes|disseny de software|requisits del software|gestio i administracio de bases de dades|test i qualitat del software|gestio del desenvolupament del software|models de qualitat en la gestio de les tic|arquitectura i tecnologies de software|laboratori integrat de software|analisi i disseny d'algorismes|coneixement raonament i incertesa|aprenentatge computacional|visualitzacio grafica interactiva|compiladors|visio per computador|robotica, lenguatge i planificacio|sistemes multimedia|fonaments de tecnologia de la informacio|sistemes d'informacio|sistemes distribuïts|disseny del software|infraestructura i tecnologia de xarxes|tecnologies avançades dinternet|sistemes i tecnologies web|garantia de la informacio i seguretat|sistemes encastats|gestio i administracio de xarxes|arquitectures avançades|microprocessadors i periferics|computacio d'altes prestacions|integracio hardware software|prototipatge de sistemes encastats|gestio de projectes)"

language_regex = "(?:(catala| ?cat ?)|(castella|castellano|español| ?esp ?)|(angles|english| ?eng ))" #50%
mention_regex = "(?:(?:mencio)?(?: en | de )?(?:enginyeria del? |tecnologies de la )?(computacio|software|computadors|informacio))" #done
professor_regex = ""
semester_regex = "(?:((primer|1er|1r?)|(segon|2n|2n?)) (?:semestre|quatrimestre|periode))" #done 
term_regex = "(parcials|finals)" #done
year_regex = "(?:(aquest )?(?:any )(\\d{2|)?(que ve|següent)?(?: any)?)" #done
username_regex = "(?:(?:soc|soc)(?: el| en)?|el meu nom (?:es |es )|em dic )([^|\s]*)" #done


entities_dict = {
    #TODO: words must be more than one
    'academic': ['expedient academic', 'expedient academic', 'expedient'],
    'exams': ['examens', 'examen', 'examens', 'examen','proves', 'parcials', 'finals'],
    'exchange': ['estudiar fora', 'erasmus', 'exchange', 'sicue', 'destinacions', 'mobilitat', 'programa mobilitat', 'marxar fora'],
    'internship': ['practiques', 'practiques', 'practicum', 'internship', 'estades', 'empresa', 'empreses'],
    'registration': ['matricula', 'matricula', 'matricular-me', 'matricules', 'matriculacio'],
    'schedule': ['horari', 'horaris', 'hores', 'franjes'],
    'calendar': ['data', 'dates', 'dia', 'dies', 'setmana', 'setmanes'],
    'teaching_guide': ['guia docent', 'guia', 'docent', 'franjes'],
    'permanence': ['regim de permanencia', 'permanencia', "fer fora"],
    'procedures': ['tramit', 'tramits', 'tramit', 'tramits', 'gestio academica', 'gestio academica'],
    'credit_recognition': ['reconeixament de credits', 'reconaixament de credits'],
    'tfg': ['tfg', 'treball final'],
    'coordination': ['coordinacio', 'coordinacio', 'cordinadors', 'cordina'],
    'start' : ['començar']
}

sub_entities_dict = {
    'tfg': {
        'tfg_aim': ['objectiu'],
        'tfg_duration': ['duracio', 'duracio', 'durada'],
        'tfg_description': ['que es el tfg', 'per que serveix'], 
        'tfg_group': ['grup', 'companys', 'gent', "mes d'un"],
        'tfg_company': ['empresa', "proposta d'empresa"],
        'tfg_matriculation': ['matricula', 'inscripcio', 'matricular-me'],
        'tfg_proposals': ['propostes' 'propostes professors'],
        'tfg_autoproposal': ['meva proposta'],
        'tfg_manyproposals': ['quantes propostes'],
        'tfg_professor': ['docent', 'tutor', 'professor', 'professora'],
        'tfg_changeproposal': ['canvi de proposta'],
        'tfg_calendar': ['temps', 'setmanes', 'calendari', 'dates'],
        'tfg_deadline': ['termini', 'final', 'entrega'],
        'tfg_tool': ['aplicacio', 'eina'],
        'tfg_steps': ['fases', 'passos'],
        'tfg_deliveries': ['entregues', 'seguiment'],
        'tfg_final_delivery': ['lliurament final', 'entrega final'],
        'tfg_avaluation': ['avaluacio', 'avaluacio', 'nota'],
        'tfg_minimumgrade': ['nota minima', 'minima nota'], 
    },    
    'internship' : {
        'internship_description': ['que es', 'que es'],
        'internship_hours': ['hores', 'quantes'],
        'internship_period': ['quant', 'quan'],
        'internship_whenstart': ['quan es comença', 'començament', 'inici'],
        'internship_steps': ['fases', 'seguiment', 'passos', 'pasos'],
        'internship_maxhours': ['maxim', 'maximes'],
        'internship_salary': ['remunerades', 'remuneracio', 'cobrar', 'diners'],
        'internship_aboard': ['a fora', 'exterior', 'pais', 'extranger'],
        'internship_moreinfo': ['informacio', 'mes'],
    },
    'registration': {
        "registration_link": ["enllaç", "pagina", "link", "pagines"],
        "registration_steps": ["pasos", "seguir", "pas"],
        "registration_date": ["dates", "data", "termini", "terminis", "calendari"],
        "registration_documentation": ["documentacio", "papers", "tramits"],
        "registration_payment": ["pagament", "diners", "pago", "pagar"],
        "registration_faqs": ["dubtes", "dubte"]
    },
    'exchange': {
        "exchange_link": ["enllaç", "pagina", "link", "pagines"],
        "exchange_destinations": ["destinacions", "destinacio", "lloc", "llocs"],
        "exchange_erasmus": ["erasmus"],
        "exchange_exchange": ["exchange"],
        "exchange_sicue": ["sicue"],
        "exchange_info": ["informacio"],
        "exchange_calendar": ["dates", "data", "termini", "terminis", "calendari"],
        "exchange_documentation": ["documentacio", "papers", "tramits"],
        "exchange_language_valoration": ["llengues", "llenguatges", "idiomes"]
    },
    'permanence': {
        "permanence_link": ["enllaç", "pagina", "link", "pagines"],
        "permanence_steps": ["pasos", "seguir"],
        "permanence_date": ["dates", "data", "termini", "terminis", "calendari"],
        "permanence_documentation": ["documentacio", "papers", "tramits"],
        "permanence_faqs": ["faqs", "preguntes"],
        "permanence_payment": ["dubtes"] 
    },
    'credit_recognition': {
        "credit_recognition_link": ["enllaç", "pagina", "link", "pagines", "dubtes", "dubte", "pregunta"],
        "credit_recognition_requirements": ["seguir", "condicions", "condició", "requeriments"],
        "credit_recognition_request": ["pasos", "peticio", "demanar", "com"]
    }
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
    m = re.search(degree_regex, query)

    if m:
        query = query.replace(m.group(0), "")
        if m.group(1):
            degree = m.group(1)
        return [function_name, degree]
    return None


def _entity_mention(query: str) -> str:
    function_name = sys._getframe(  ).f_code.co_name.replace("_entity_","")
    m = re.search(mention_regex, query)

    if m:
        query = query.replace(m.group(0), "")
        if m.group(1):
            if 'tic' in m.group(1) or 'informacio' == m.group(1):
                mention = 'tic'
            elif 'es' in m.group(1) or 'software' == m.group(1):
                mention = 'es'
            elif 'comp' in m.group(1) or 'computacio' == m.group(1):
                mention = 'comp'
            elif 'ec' in m.group(1) or 'computadors' == m.group(1):
                mention = 'ec'
        return [function_name, mention]
    return None


def _entity_subject(query: str) -> str:
    function_name = sys._getframe(  ).f_code.co_name.replace("_entity_","")
    m = re.search(subject_regex, query)

    if m:
        query = query.replace(m.group(0), "")
        if m.group(1):
            subject = m.group(1)
        return [function_name, subject]
    return None


def _entity_semester(query: str) -> str:
    function_name = sys._getframe(  ).f_code.co_name.replace("_entity_","")
    query = utils.words_to_nums(query)
    m = re.search(semester_regex, query)

    if m:
        query = query.replace(m.group(0), "")
        if m.group(1):
            semester = m.group(1)
        return [function_name, semester]
    return None


def _entity_term(query: str) -> str:
    function_name = sys._getframe(  ).f_code.co_name.replace("_entity_","")
    m = re.search(term_regex, query)

    if m:
        query = query.replace(m.group(0), "")
        if m.group(1):
            term = m.group(1)
        return [function_name, term]
    return None


def _entity_language(query: str) -> str:
    function_name = sys._getframe(  ).f_code.co_name.replace("_entity_","")
    m = re.search(language_regex, query)
    language = 'cat'
    if m:
        query = query.replace(m.group(0), "")
        if m.group(1):
            language = 'cat'
        elif m.group(2):
            language = 'esp'
        elif m.group(3):
            language = 'eng'
        return [function_name, language]
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
#     m = re.search(degree_regex, query)

#     if m:
#         query = query.replace(m.group(0), "")
#         if m.group(1):
#             professor = m.group(1)
#         return [function_name, professor]
#     return None


def _entity_username(query: str) -> str:
    function_name = sys._getframe(  ).f_code.co_name.replace("_entity_","")
    username = 'Goffy'
    m = re.search(username_regex, query)

    if m:
        query = query.replace(m.group(0), "")
        if m.group(1):
            username = m.group(1)
        return [function_name, username]
    return None


def _entity_year(query: str) -> str:
    function_name = sys._getframe(  ).f_code.co_name.replace("_entity_","")

    m = re.search(year_regex, query)
    this_year = date.today().year
    year = "" 

    if m:
        query = query.replace(m.group(0), "")
        if m.group(2):
            year = m.group(2) if len(year) == 4 else "20" + str(m.group(2))
 
        elif m.group(3):
            year = this_year + 1

        elif m.group(1):
            year = this_year

        return [function_name, str(year)]
    return None


def _entity(query: str) -> list:
    entities_found = []
    query = utils.preprocess(query)    
    query = utils.query_to_list(query)

    for entity in entities_dict:
        if any(word in query for word in entities_dict[entity]):
            entities_found.append([entity, True])  

    return entities_found #TODO: sorted list


def _sub_entity(query: list) -> list:
    sub_entities_found = []
    query = utils.preprocess(query)    
    query = utils.query_to_list(query)

    for entity in sub_entities_dict:
        for sub_entity in sub_entities_dict[entity]:
            if any(word in query for word in sub_entities_dict[entity][sub_entity]):
                sub_entities_found.append([sub_entity, True])  

    return sub_entities_found #TODO: sorted list


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
    sub_entities_list = []

    for function in function_list:
        entity = function(query)
        if entity != None:
            entities_list.append(entity)

    sub_entities_list = _sub_entity(query) #TODO

    return entities_list, sub_entities_list #TODO: sorted list






