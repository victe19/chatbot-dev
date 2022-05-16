import random
import re
from bot.src.context import Context
import bot.src.utils.utils as utils
import bot.data as data
from db.main import get_from_db


def get_teacher_office(profe: str, room: str):
    pass 

def get_degree_shedule(degree, course, semester):
    subject_dict = get_from_db('degrees', degree)
    return subject_dict[course][semester]

def generate(action: str, context: Context()) -> str:    
    if action == 'teacher_office':
        return get_teacher_office(1) #(contex.profe)

    elif action == 'shedule':
        return get_degree_shedule(context.degree, context.course, context.semester)

    responses = utils.json_parser("bot/data/responses.json")
    answer_list = responses.get(action)["answers"]
    answer = answer_list[random.randint(0, len(answer_list)-1)]

    reply = answer.format(context.username)

    return reply
    