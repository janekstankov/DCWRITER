import time
from discord.ext import commands
import os
from colorama import *
import ctypes
import random
import string

clear = lambda: os.system('cls')

print(f'{Fore.GREEN}Hi!')
clear()

def intro():
    print(Fore.RED + """\
██████╗  ██████╗██╗    ██╗██████╗ ██╗████████╗███████╗██████╗ 
██╔══██╗██╔════╝██║    ██║██╔══██╗██║╚══██╔══╝██╔════╝██╔══██╗
██║  ██║██║     ██║ █╗ ██║██████╔╝██║   ██║   █████╗  ██████╔╝
██║  ██║██║     ██║███╗██║██╔══██╗██║   ██║   ██╔══╝  ██╔══██╗
██████╔╝╚██████╗╚███╔███╔╝██║  ██║██║   ██║   ███████╗██║  ██║
╚═════╝  ╚═════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                                            """ + Fore.RESET)



ctypes.windll.kernel32.SetConsoleTitleW(f" ;) ")
intro()
if os.path.exists("token.txt"):
    print(Fore.GREEN + time.strftime("[%H:%M:%S]", time.localtime()) + f' Found Token!')
else:
    token_int = input(Fore.YELLOW + time.strftime("[%H:%M:%S]", time.localtime()) + f' Past your token (without ""): {Fore.BLUE}')
    a = open("token.txt", "a")
    a.write(f'{token_int}')
    a.close()


x = open('token.txt')
token = x.readline()

time.sleep(2)
clear()
intro()
print(Fore.YELLOW + time.strftime("[%H:%M:%S]", time.localtime()) + f' Logging to your account...')

bot = commands.Bot(command_prefix=".", self_bot=True)
writed_message = 0
write_status = 0

while 1:
    try:
        @bot.event
        async def on_connect():
            print(Fore.LIGHTBLUE_EX + time.strftime("[%H:%M:%S] ",time.localtime()) + f"{Fore.GREEN}Bot is ready! Welcome {bot.user}({bot.user.id})! Write $write - to any chat to start spam! $stop to stop program.")


        @bot.event
        async def on_message(message):
            global writed_message, write_status
            if message.author == bot.user:
                if message.content.startswith('$write'):
                    if write_status == 0:
                        print(Fore.LIGHTBLUE_EX + time.strftime("[%H:%M:%S] ",time.localtime()) + f'{Fore.GREEN}writing ;)')
                        start = time.time()
                        write_status += 1
                        while True:
                            time.sleep(0.65)
                            randomnumber = random.randint(1,128)
                            code = (('').join(random.choices(string.ascii_letters + string.digits, k=randomnumber)))
                            channel = message.channel
                            await channel.send(code)
                            check_time = time.time() - start
                            tz = time.strftime("%H:%M:%S", time.gmtime(check_time))
                            ctypes.windll.kernel32.SetConsoleTitleW(
                                f"DCWRITER | Time: {tz} | Sended Messages: {writed_message}")
                            writed_message += 1
                    else:
                        await message.channel.send('Im already writing stupid asshole...')
                        print(Fore.LIGHTBLUE_EX + time.strftime("[%H:%M:%S] ", time.localtime()) + f'{Fore.RED}Im already writing retard...')




        bot.run(token, bot=False)
    except:
        print(f'{Fore.RED}error!')
        exit()
stop = time.time()
elapsed_time = time.time() - start
t = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
