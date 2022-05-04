import threading
from colorama import Fore
from time import *
from util.common import *

setTitle(f'Cookies CCV Stealer') # Change title
clear() # Clear console to stop colorama buggin

threads = [] # Set threads to 0

print(banner)
thread_ammount = int(input(f"{Fore.GREEN}Thread Ammount >> {Fore.RESET}")) # Enter thread ammount into console
input(f"\n{Fore.CYAN}Press enter to start stealer. . .{Fore.RESET}")
clear()


def run_stealer():
    for i in range(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999): # Use for loop since its ALOT faster than a while loop
        CCV = random_VISA_generator() # Get random VISA CCV
        bal = random_balance_generator() # Get random balance
        date = random_expire_date_generator() # Get random expire date
        CVV = random_CVV_generator() # Get random CVV
        if random.random() < percentage_chance:
            print(f"\n\n{Fore.LIGHTCYAN_EX}CRACKED CCV!!!{Fore.RESET}")
            print(f"{Fore.GREEN}{starterValid}{CCV} {date} {CVV} [Valid]{Fore.RESET}")
            write_CCV_info(CCV, bal, date, CVV) # Write CCV info to txt file
        else:
            print(f"{Fore.RESET}{starterInvalid}{CCV} {date} {CVV} [Invalid]{Fore.RESET}")


# Set threads
for i in range(thread_ammount):
    t = threading.Thread(target=run_stealer)
    t.daemon = True
    threads.append(t)

# Start threads
for i in range(thread_ammount):
    threads[i].start()

# Join threads
for i in range(thread_ammount):
    threads[i].join()


