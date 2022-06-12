import os

import bot.src.flowbot as bot
from colorama import Fore

from context import Context

# Get environment variables
PYTHONPATH = os.getenv('PYTHONPATH')

context = Context()

while 1:
    query = input(f"{Fore.GREEN}User:{Fore.WHITE} ")
    reply = bot.message(query, context)
    print(f"{Fore.YELLOW}Bot:{Fore.WHITE} {reply}")
