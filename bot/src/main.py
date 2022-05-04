from colorama import Fore, Style

import bot
from context import Context

context = Context()

while 1:
    query = input(f"{Fore.GREEN}User:{Fore.WHITE} ")
    reply = bot.message(query, context)
    print(f"{Fore.YELLOW}Bot:{Fore.WHITE} {reply}")
