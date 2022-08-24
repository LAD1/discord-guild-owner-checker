from colorama import Fore, Back, Style
import httpx

with open("tkns.txt", "r+") as f:
    lines = f.readlines()

for line in lines:
    token = line.strip()
    headers = {'Authorization': token}
    try:
        r = httpx.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers=headers)
        print("Running on token: " + token)
    except:
        print("Error on token: " + token)
        continue
    guilds = r.json()
    for guild in guilds:
        if guild["owner"]:
            print(Fore.GREEN+f"[+] Owner of {guild['name']} | ID: {guild['id']} | Members: {guild['approximate_member_count']} | Token: {token}"+Fore.RESET)
            with open("owner.txt", "a", encoding="utf8", errors="ignore") as f: f.write(f"[+] Owner of {guild['name']} | ID: {guild['id']} | Members: {guild['approximate_member_count']} | Token: {token}\n")
        else:
            print(Fore.RED+f"[-] Not owner of {guild['name']} | ID: {guild['id']} | Members: {guild['approximate_member_count']} | Token: {token}"+Fore.RESET)
            with open("notowner.txt", "a", encoding="utf8", errors="ignore") as f: f.write(f"[-] Not owner of {guild['name']} | ID: {guild['id']} | Members: {guild['approximate_member_count']} | Token: {token}\n")
