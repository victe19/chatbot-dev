import inspect
import re
import sys
from datetime import date
import bot.src.utils.utils as utils
import dialogue_manager as dm

degree_core_regex = "(aeronautica|dades|electronica|artificial|informatica|quimica|ciutats|telecomunicacions|telecos)" #done
degree_regex = "(?:grau|carrera)?(?: en | de | d')?(?:enginyeria)?(?: de| en)?" + degree_core_regex #done
course_regex = "((?:primer|segon|tercer|quart)|[1-4](?:r|n|t)?)(?: curs| any)" #done
subject_regex = "(algebra|calcul|electricitat i electronica|fonaments dels computadors|fonaments d'informatica|matematica discreta|metodologia de la programacio|organitzacio i gestio d'empreses|fonaments d'enginyeria|estadistica|arquitectura de computadors|bases de dades|enginyeria del software|estructura de computadors|informacio i seguretat|intel·ligencia artificial|laboratori de programacio|sistemes operatius|xarxes|disseny de software|requisits del software|gestio i administracio de bases de dades|test i qualitat del software|gestio del desenvolupament del software|models de qualitat en la gestio de les tic|arquitectura i tecnologies de software|laboratori integrat de software|analisi i disseny d'algorismes|coneixement raonament i incertesa|aprenentatge computacional|visualitzacio grafica interactiva|compiladors|visio per computador|robotica, lenguatge i planificacio|sistemes multimedia|fonaments de tecnologia de la informacio|sistemes d'informacio|sistemes distribuïts|disseny del software|infraestructura i tecnologia de xarxes|tecnologies avançades dinternet|sistemes i tecnologies web|garantia de la informacio i seguretat|sistemes encastats|gestio i administracio de xarxes|arquitectures avançades|microprocessadors i periferics|computacio d'altes prestacions|integracio hardware software|prototipatge de sistemes encastats|gestio de projectes)"

language_regex = "(?:(catala| ?cat ?)|(castella|castellano|español| ?esp ?))" #50%
mention_regex = "(?:(?:mencio)?(?: en | de )?(?:enginyeria del? |tecnologies de la )?(computacio|software|computadors|informacio))" #done
semester_regex = "(?:((primer|1er|1r?)|(segon|2n|2n?)) (?:semestre|quatrimestre|periode))" #done 
term_regex = "(parcials|finals)" #done
username_regex = "(?:(?:soc|soc)(?: el| en)?|el meu nom (?:es |es )|em dic )([^|\s]*)" #done


entities_dict = {
    'cat': {
        'academic': ['expedient academic', 'expedient academic', 'expedient'],
        'exams': ['examens', 'examen', 'examens', 'examen','proves', 'parcials', 'finals'],
        'exchange': ['estudiar fora', 'erasmus', 'exchange', 'sicue', 'destinacions', 'mobilitat', 'programa mobilitat', 'marxar fora'],
        'internship': ['practiques', 'practiques', 'practicum', 'internship', 'estades', 'empresa', 'empreses'],
        'registration': ['matricula', 'matricula', 'matricular-me', 'matricules', 'matriculacio'],
        'schedule': ['horari', 'horaris', 'hores', 'franjes'],
        'teaching_guide': ['guia docent', 'guia', 'docent', 'franjes'],
        'permanence': ['regim de permanencia', 'permanencia', "fer fora"],
        'procedures': ['tramit', 'tramits', 'tramit', 'tramits', 'gestio academica', 'gestio academica'],
        'credit_recognition': ['reconeixament de credits', 'reconaixament de credits'],
        'tfg': ['tfg', 'treball final'],
        'coordination': ['coordinacio', 'coordinacio', 'cordinadors', 'cordina'],
        'start' : ['començar']
    }, 
    'esp': {
        'academic': ['expediente academico', 'expediente academico', 'expediente'],
        'exams': ['examenes', 'examen', 'examenes', 'examen','pruebas', 'parciales', 'finales'],
        'exchange': ['estudiar fuera', 'erasmus', 'exchange', 'sicue', 'destinos', 'movilidad', 'programa movilidad', 'marchar fuera'],
        'internship': ['practicas', 'practicas', 'practicum', 'internship', 'estancias', 'empresa', 'empresas'],
        'registration': ['matricula', 'matricula', 'matricularme', 'matriculas', 'matriculacion'],
        'schedule': ['horario', 'horarios', 'horas', 'franjas'],
        'teaching_guide': ['guía docente', 'guía', 'docente', 'franjas'],
        'permanence': ['regimen de permanencia', 'permanencia', "echar"],
        'procedures': ['tramite', 'tramites', 'tramite', 'tramites', 'gestion academica', 'gestio academica'],
        'credit_recognition': ['reconocimiento de créditos', 'reconocimiento de creditos'],
        'tfg': ['tfg', 'trabajo final'],
        'coordination': ['coordinación', 'coordinacion', 'cordinadores', 'cordina'],
        'start' : ['empezar']
    }
}


sub_entities_dict = {
    'cat': {
        'tfg': {
            'tfg_aim': ['objectiu', 'finalitat'],
            'tfg_duration': ['duracio', 'duracio', 'durada', 'dura', 'temps per fer'],
            'tfg_description': ['que es el tfg', 'per que serveix'], 
            'tfg_group': ['companys', 'gent', "mes d'un", 'cooperatiu', 'en grup'],
            'tfg_company': ['fer amb empresa', "propostes d'empresa", "proposta d'empresa", 'on treballo', 'practiques'],
            'tfg_matriculation': ['matricula', 'inscripcio', 'matricular-me', 'matricules', 'matricular'],
            'tfg_proposals': ['propostes', 'propostes professors', 'proposta', 'ofertes'],
            'tfg_autoproposal': ['meva proposta', 'idea meva', 'proposta meva', 'puc fer una proposta', 'puc proposar'],
            'tfg_manyproposals': ['quantes propostes', 'triar', 'propostes maximes'],
            'tfg_professor': ['docent', 'tutor', 'professor', 'professora', 'el que em porta', 'tutoria'],
            'tfg_changeproposal': ['canvi de proposta', 'canvi proposta inicial'],
            'tfg_calendar': ['setmanes', 'calendari', 'dates', 'data', 'roadmap', 'temps'],
            'tfg_deadline': ['termini', 'entrega final', "quan s'entrega"],
            'tfg_tool': ['aplicacio', 'eina', 'app'],
            'tfg_steps': ['fases', 'passos', 'desenvolupament'],
            'tfg_deliveries': ['entregues', 'seguiment', 'informes', 'com es lliuren', 'com puc lliurar-los'],
            'tfg_final_delivery': ['lliurament final', 'entrega final'],
            'tfg_avaluation': ['avaluacio', 'avaluacio', 'nota final', 'nota tfg', 'evaluar', "s'evalua", 'avaluar' ],
            'tfg_delivery_grade': ['nota informes', 'nota entregues', 'nota seguiment'],
            'tfg_minimumgrade': ['nota minima', 'minima nota'],
            'tfg_faqs': ['dubtes', 'dubte', 'faqs'] 
        },    
        'internship' : {
            'intership_link': ['enllaç'],
            'internship_description': ['que es', 'que es', 'que es fa', "que s'ha de fer", "que son", 'descripcio'],
            'internship_hours': ['quentes hores', 'hores', 'dura'],
            'internship_period': ['quant', 'quan'],
            'internship_whenstart': ['quan es comença', 'començament', 'inici'],
            'internship_steps': ['fases', 'passos', 'passos', 'matricular-me', 'que he de fer', "com s'ha de fer"],
            'internship_salary': ['remunerades', 'remuneracio', 'cobrar', 'diners', 'salari', 'cobro', 'diner', 'paguen'],
            'internship_moreinfo': ['informacio', 'dubtes', 'dubte', 'saber mes', 'pregunta', 'preguntes'],
            'internship_offers': ['oferta', 'ofertes', 'empresa', 'empreses', 'opcions', 'laboral', 'on puc fer'],
            'internship_ownoffers': ['trobo jo', 'buscar jo', 'oferta meva', 'propia oferta'],
            'internship_workleave': ['permis', 'permisos', 'justificant', 'justificants'],
            'internship_folowup': ['tutor', 'tutora', 'seguiment', 'tutoria', 'professor', 'tutoria', 'supervisa'],
            'internship_evaluation': ['evaluacio', 'avaluacio', 'nota', 'notes'],
        },
        'registration': {
            "registration_link": ["enllaç", "pagina", "link", "pagines"],
            "registration_steps": ["passos", "seguir", "pas", "que he de fer"],
            "registration_date": ["dates", "data", "termini", "terminis", "calendari"],
            "registration_documentation": ["documentacio", "papers", "tramits"],
            "registration_payment": ["pagament", "diners", "pago", "pagar"],
            "registration_faqs": ["dubtes", "dubte", "preguntes"]
        },
        'exchange': {
            "exchange_link": ["enllaç", "pagina", "link", "pagines", 'web'],
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
            "permanence_documentation": ["documentacio", "normativa", "document"],
            "permanence_faqs": ["faqs", "preguntes", "pregunta", 'dubte', 'dubtes'],
        },
        'credit_recognition': {
        "credit_recognition_link": ["enllaç", "pagina", "link", "pagines", "dubtes", "dubte", "pregunta"],
        "credit_recognition_requirements": ["seguir", "condicions", "condició", "requeriments"],
        "credit_recognition_request": ["passos", "peticio", "demanar"]
        }
    },
    'esp': {
        'tfg': {
            'tfg_aim': ['objetivo', 'finalidad'],
            'tfg_duration': ['duracion', 'duracion', 'duración', 'dura', 'tiempo por hacer'],
            'tfg_description': ['que es el tfg', 'para que sirve'], 
            'tfg_group': ['compañeros', 'gente', "mas de uno", 'cooperativo', 'en grupo'],
            'tfg_company': ['hacer con empresa', "propuestas de empresa", "propuesta de empresa", 'donde trabajo', 'practicas'],
            'tfg_matriculation': ['matricula', 'inscripcion', 'matricularme', 'matriculas', 'matricular'],
            'tfg_proposals': ['propuestas', 'propuestas profesores', 'propuesta', 'ofertas'],
            'tfg_autoproposal': ['mi propuesta', 'idea mía', 'propuesta mía', 'puedo hacer una propuesta', 'puedo proponer'],
            'tfg_manyproposals': ['cuántas propuestas', 'elegir', 'propuestas maximas'],
            'tfg_professor': ['docente', 'tutor', 'profesor', 'profesora', 'lo que me lleva', 'tutoría'],
            'tfg_changeproposal': ['cambio de propuesta', 'cambio propuesta inicial'],
            'tfg_calendar': ['semanas', 'calendario', 'fechas', 'fecha', 'roadmap', 'tiempo'],
            'tfg_deadline': ['plazo', 'entrega final', "cuando se entrega"],
            'tfg_tool': ['aplicación', 'herramienta', 'app'],
            'tfg_steps': ['fases', 'pasos', 'desarrollo'],
            'tfg_deliveries': ['entregas', 'seguimiento', 'informes', 'cómo se entregan', 'cómo puedo entregarlos'],
            'tfg_final_delivery': ['entrega final', 'entrega final'],
            'tfg_avaluation': ['evaluacion', 'evaluacion', 'nota final', 'nota tfg', 'evaluar', "se evalúa", 'evaluar'],
            'tfg_delivery_grade': ['nota informes', 'nota entregas', 'nota seguimiento'],
            'tfg_minimumgrade': ['nota minima', 'minima nota'],
            'tfg_faqs': ['dudas', 'duda', 'faqs'] 
        },    
        'internship' : {
            'intership_link': ['enlace'],
            'internship_description': ['que se', 'que se', 'que se hace', "que se debe hacer", "que son", 'descripcion'],
            'internship_hours': ['quentes horas', 'horas', 'dura'],
            'internship_period': ['cuánto', 'cuándo'],
            'internship_whenstart': ['cuando se comienza', 'comienzo', 'inicio'],
            'internship_steps': ['fases', 'pasos', 'pasos', 'matricularme', 'que debo hacer', "cómo se debe hacer"],
            'internship_salary': ['remuneradas', 'remuneracio', 'cobrar', 'dinero', 'salario', 'cobro', 'dinero', 'pagan'],
            'internship_moreinfo': ['informacion', 'dudas', 'duda', 'saber mas', 'pregunta', 'preguntas'],
            'internship_offers': ['oferta', 'ofertas', 'empresa', 'empresas', 'opciones', 'laboral', 'donde puedo hacer'],
            'internship_ownoffers': ['encuentro yo', 'buscar yo', 'oferta mía', 'propia oferta'],
            'internship_workleave': ['permiso', 'permisos', 'justificante', 'justificantes'],
            'internship_folowup': ['tutor', 'tutora', 'seguimiento', 'tutoría', 'profesor', 'tutoría', 'supervisa'],
            'internship_evaluation': ['evaluacion', 'evaluacion', 'nota', 'notas'],
        },
        'registration': {
            "registration_link": ["enlace", "pagina", "link", "paginas"],
            "registration_steps": ["pasos", "seguir", "paso", "que debo hacer"],
            "registration_date": ["fechas", "fecha", "plazo", "plazos", "calendario"],
            "registration_documentation": ["documentacion", "papeles", "tramitos"],
            "registration_payment": ["pago", "dinero", "pago", "pagar"],
            "registration_faqs": ["dudas", "duda", "preguntas"]
        },
        'exchange': {
            "exchange_link": ["enlace", "pagina", "link", "paginas", 'web'],
            "exchange_destinations": ["destinos", "destino", "lugar", "lugares"],
            "exchange_erasmus": ["erasmus"],
            "exchange_exchange": ["exchange"],
            "exchange_sicue": ["sicue"],
            "exchange_info": ["información"],
            "exchange_calendar": ["fechas", "fecha", "plazo", "plazos", "calendario"],
            "exchange_documentation": ["documentacion", "papeles", "tramitos"],
            "exchange_language_valoration": ["lenguas", "lenguajes", "idiomas"]
        },
        'permanence': {
            "permanence_link": ["enlace", "pagina", "link", "paginas"],
            "permanence_documentation": ["documentacion", "normativa", "documento"],
            "permanence_faqs": ["faqs", "preguntas", "pregunta", 'duda', 'dudas'],
        },
        'credit_recognition': {
            "credit_recognition_link": ["enlace", "pagina", "link", "paginas", "dudas", "duda", "pregunta"],
            "credit_recognition_requirements": ["seguir", "condiciones", "condición", "requerimientos"],
            "credit_recognition_request": ["pasos", "peticio", "pedir"]
        }
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
        return [function_name, language]
    return None


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


def _entity(query: str, lang) -> list:
    entities_found = []
    query = utils.preprocess(query)    
    query = utils.query_to_list(query)

    for entity in entities_dict[lang]:
        for word in entities_dict[lang][entity]:

            if " " in word:
                if all(split_words in query for split_words in word.split()):
                    entities_found.append([entity, True]) 
        if entities_found == []:

            if any(word in query for word in entities_dict[lang][entity]):
                entities_found.append([entity, True]) 
        
    return entities_found


def _sub_entity(query: list, lang) -> list:
    sub_entities_found = []
    query = utils.preprocess(query)    
    query = utils.query_to_list(query)

    for entity in sub_entities_dict[lang]:
        for sub_entity in sub_entities_dict[lang][entity]:
            for word in sub_entities_dict[lang][entity][sub_entity]:
                if " " in word:
                    if all(split_words in query for split_words in word.split()):
                        sub_entities_found.append([sub_entity, True])
            if any(word in query for word in sub_entities_dict[lang][entity][sub_entity]):
                sub_entities_found.append([sub_entity, True])  

    return sub_entities_found


def get_module_functions() -> list:
    module_functions = dir(sys.modules[__name__])
    module_core_functions = []
    for function in module_functions:
        if '_entity_' in function:
            module_core_functions.append(eval(function))

    return module_core_functions


def entities_extraction(query: str, lang) -> list:
    function_list = get_module_functions()
    entities_list = _entity(query, lang)
    sub_entities_list = []

    for function in function_list:
        entity = function(query)
        if entity != None:
            entities_list.append(entity)

    sub_entities_list = _sub_entity(query, lang)

    return entities_list, sub_entities_list #TODO: sorted list






