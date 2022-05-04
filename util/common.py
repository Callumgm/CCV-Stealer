import os, sys, platform, ctypes, random, string
from time import sleep
from colorama import Fore

percentage_chance = 0.0001 # The chance of "finding a valid CCV"

# Clear console
def clear():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    elif system == 'Linux':
        os.system('clear')
    else:
        print('\n')*120
    return

# Set console title
def setTitle(str):
    system = platform.system()
    if system == 'Windows':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{str} | CookiesKush420")
    else:
        os.system(f"\033]0;{str}\a")

# Print slow (animation)
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter);sys.stdout.flush();sleep(0.05)

# Gen random CCV
def random_VISA_generator():
    chars = string.digits
    start = "VISA 4"
    return start + ''.join(random.choice(chars) for x in range(15))

# Gen random expire date
def random_expire_date_generator():
    expire_date = random.randint(2022,2026)
    return expire_date

# Gen random balance
def random_balance_generator():
    bal = random.randint(10, 348)
    return bal

# Gen random CVV
def random_CVV_generator():
    bal = random.randint(100, 999)
    return bal

# Write "found" CCV to txt file
def write_CCV_info(CCV, bal, date, CVV):
    with open("CCV-Info.txt", "a+") as f:
        f.writelines(f"\n----------------------------------------\nCCV: {CCV}\nBalance: {bal} \nExpire Date: {date} \nCVV: {CVV}")
    f.close()

# Simple banner
banner = f"""

    {Fore.LIGHTMAGENTA_EX}Welcome to Cookies CCV Stealer
        {Fore.LIGHTBLUE_EX}github.com/callumgm

{Fore.RESET}"""

starterInvalid = f"[{Fore.RED}-{Fore.RESET}] Card Type: "
starterValid = f"[{Fore.GREEN}X{Fore.RESET}] Card Type: "