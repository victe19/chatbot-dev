import re

import utils

degrees_core_regex = "(?: ?(dades|(?:sistemes|electrònica) de telecomunicació|telecos|informàtica|info |química|gestió aeronàutica))"
degrees_regex = "(?:grau|carrera)?(?: en | de | d')?(?:enginyeria)?(?: de| en)?" + degrees_core_regex

departaments_regex = "(departament)( de)? (|)"
mencions_regex = "(menció)( en | de )? (computació|enginyeria del? (software|computadors)|tecnologies de la informació)"
professors_regex = ""
course_regex = "((?:primer|segon|tercer|quart)|[1-4](?:r|n|t)?)(?: curs| any)"
year_regex = "(any )?(\\d{2,4})( any)?"
semester_regex = "((primer|1er|1)|(segon|2n|2))(semestre|quatrimestre|període)" 


def extract_entity_course(query: str) -> str:
    query = utils.words_to_nums(query)
    m = re.search(course_regex, query)

    if m:
        query = query.replace(m.group(0), "")
        if m.group(1):
            course = m.group(1)
        return course
    return None


def extract_entity_degree(query: str) -> str:
    m = re.search(degrees_regex, query)

    if m:
        query = query.replace(m.group(0), "")
        if m.group(1):
            degree = m.group(1)
        return degree
    return None