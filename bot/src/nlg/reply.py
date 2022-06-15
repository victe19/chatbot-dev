import random
import re
from bot.src.context import Context
import bot.src.utils.utils as utils
import bot.data as data
# from db.main import get_from_db
import json


def get_teacher_office(profe: str, room: str):
    pass 


def get_degree_schedule(degree, course, semester, mention = None):
    # subject_dict = get_from_db('degrees', degree)

    with open(f"bot/data/{degree}.json") as f:
        subject_dict = json.load(f)
    
    if mention is None:
        schedule = subject_dict['schedule'][course][semester]
    else:
        schedule = subject_dict['schedule'][course][semester][mention]

    return schedule


def get_degree_exams(degree, semester, term):
    # subject_dict = get_from_db('degrees', degree)

    with open(f"bot/data/{degree}.json") as f:
        subject_dict = json.load(f)

    return subject_dict['exams'][semester][term]


def get_tfg_info(sub_entity_list):
    # subject_dict = get_from_db('degrees', degree)

    with open("bot/data/general.json") as f:
        subject_dict = json.load(f)

    return subject_dict['treball final de grau'][sub_entity_list]


def get_internship_info(sub_entity_list):
    # subject_dict = get_from_db('degrees', degree)

    with open("bot/data/general.json") as f:
        subject_dict = json.load(f)

    return subject_dict['practiques externes']['extracurricular'][sub_entity_list]


def get_teaching_guide(degree, subject):
    # subject_dict = get_from_db('degrees', degree)

    with open(f"bot/data/{degree}.json") as f:
        subject_dict = json.load(f)

    return subject_dict['subjects'][subject]['teaching_guide']
    

def generate(action: str, context: Context) -> str:    
    dynamic_info = ''
    if action == 'teacher_office':
        dynamic_info = get_teacher_office(context.professor)
    
    elif action == 'schedule':
        dynamic_info = get_degree_schedule(context.degree, context.course, context.semester, context.mention)
        context.course = None
        context.semester = None
        context.mention = None
    elif action == 'exams':
        dynamic_info = get_degree_exams(context.degree, context.semester, context.term)
        # context = context.clean_context(['semester', 'term'])
        context.semester = None
        context.term = None

    elif action == 'teaching_guide':
        dynamic_info = get_teaching_guide(context.degree, context.subject)
        context.subject = None
    
    elif 'tfg' in action and action != 'ask_tfg':
        dynamic_info = get_tfg_info(action)
        action = 'nothing'
    
    elif 'internship' in action and action != 'ask_internship':
        dynamic_info = get_internship_info(action)
        action = 'nothing'
    
    responses_language = 'responses_' + context.language

    responses = utils.json_parser(f"bot/data/{responses_language}.json")
    answer_list = responses.get(action)["answers"]
    answer = answer_list[random.randint(0, len(answer_list)-1)]
    answer += dynamic_info
    reply = answer.format(context.username)

    return reply
    