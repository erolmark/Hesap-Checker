import requests

def netflix_checker():
    print("\033[91mE posta:\033[0m")
    email = input()
    print("\033[91mŞifre:\033[0m")
    password = input()
    
    url = "https://www.netflix.com/login"
    data = {"email": email, "password": password}
    response = requests.post(url, data=data)
    
    if "profile-gate-label" in response.text:
        print("\033[92mHit!\033[0m")
    else:
        print("\033[91mHesap Kötü\033[0m")

def disney_checker():
    print("\033[94mE posta:\033[0m")
    email = input()
    print("\033[94mŞifre:\033[0m")
    password = input()
    
    url = "https://www.disneyplus.com/login"
    data = {"email": email, "password": password}
    response = requests.post(url, data=data)
    
    if "btn-primary" in response.text:
        print("\033[92mHit!\033[0m")
    else:
        print("\033[91mHesap Kötü\033[0m")

def blutv_checker():
    print("\033[92mE posta:\033[0m")
    email = input()
    print("\033[92mŞifre:\033[0m")
    password = input()
    
    url = "https://www.blutv.com/login"
    data = {"email": email, "password": password}
    response = requests.post(url, data=data)
    
    if "class=\"name\">" in response.text:
        print("\033[92mHit!\033[0m")
    else:
        print("\033[91mHesap Kötü\033[0m")

print("\033[91m______           _              __        __   _\033[0m")
print("\033[91m|__  (_)_ __   __| | __ _ _ __   \ \      / /__| |__\033[0m")
print("\033[91m  / /| | '_ \ / _` |/ _` | '_ \   \ \ /\ / / _ \ '_ \033[0m")
print("\033[91m / /_| | | | | (_| | (_| | | | |   \ V  V /  __/ |_) |\033[0m")
print("\033[91m/____|_|_| |_|\__,_|\__,_|_| |_|    \_/\_/ \___|_.__/\033[0m")

print("\033[91m1-Netflix Checker (kırmızı)\033[0m")
print("\033[94m2-Disney Checker (mavi)\033[0m")
print("\033[92m3-BluTV Checker (yeşil)\033[0m")

secim = input("\033[93mSeçenek:\033[0m")
if secim == "1":
    netflix_checker()
elif secim == "2":
    disney_checker()
elif secim == "3":
    blutv_checker()
else:
    print("\033[91mGeçersiz seçenek.\033[0m")

print("\n\033[93mZindan Web by Vera Marka\033[0m")
