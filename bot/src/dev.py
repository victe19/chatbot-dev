from colorama import Fore

import bot.src.flowbot as bot
from context import Context

import os


# Get environment variables
PYTHONPATH = os.getenv('PYTHONPATH')



context = Context()

while 1:
    query = input(f"{Fore.GREEN}User:{Fore.WHITE} ")
    reply = bot.message(query, context)
    print(f"{Fore.YELLOW}Bot:{Fore.WHITE} {reply}")
