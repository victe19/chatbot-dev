import random
from bot.src.context import Context
import bot.src.utils.utils as utils
import bot.data as data

def generate(action: str, context: Context()) -> str:    
    # responses = utils.json_parser("software/bot/data/responses.json")
    responses = utils.json_parser("bot/data/responses.json")
    answer_list = responses.get(action)["answers"]
    answer = answer_list[random.randint(0, len(answer_list)-1)]

    # if context.username is not None:
    #     reply = answer.format(context.username)

    reply = answer.format(context.username)   

    return reply
    