# internal imports

import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
import pip._vendor.requests as requests
# external imports



"""
Change 4 Fields (Compulspory) | 3 Fields are optional | Sample Video on where and how to find them is available in Readme.
URL: your form url # URL must be response URL, sample is provided
REFERER: Take by Filling a response
COOKIE: Take by filling a response
DATA: Fill a form and find it :)
PROXYS: You can provide proxies also.
MAX_WORKERS: Change this value to increase the speed of spam. Don't go beyond 500.
SPAM_COUNT: Change this to increase spam count
"""

MAX_WORKERS = 10 # Change this value to increase the speed of spam. Don't go beyond 500.
SPAM_COUNT = 100 # Change this to increase spam count

URL = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSeeQGtycNnvHW42Jix9quwtltPVqG7cS0U4REP91peXrHiREA/formResponse'

DATA = 'entry.1212348438=mardi+31&dlut=1638227466505&entry.1212348438_sentinel=&fvv=1&partialResponse=%5Bnull%2Cnull%2C%22-5331645099468021118%22%5D&pageHistory=0&fbzx=-5331645099468021118'

REFERER = 'https://docs.google.com/forms/d/e/1FAIpQLSeeQGtycNnvHW42Jix9quwtltPVqG7cS0U4REP91peXrHiREA/viewform?fbzx=-5331645099468021118'

COOKIE = 'S=spreadsheet_forms=PNJjJ3zHETFvZw1iAhpJQQKoGUI1p3QGlVlzNv5Unvg; COMPASS=spreadsheet_forms=CjIACWuJVzLT06LFEHmHyTVz7bYhN3OG3Y-uWMJrHfTDdSEn0aKvGmhrlDUfxngMnPiJEBC2yZWNBho0AAlriVf2J8l8L5LjQrJJLSEkj0jU05QQrURZEqpkLJvT4LAxQiiUBb_RWBXOe1tySOlnwA==; SSID=AN6UD5mtrp5Zj7UYu; HSID=AcjB7R0raUky8t0la; APISID=0_MrLnxAd-MaA5hu/A9nMzQgzBvbr-anEY; SAPISID=K3LcRk50PtPrQJaS/AdNLhnvkACGmx_Q6v; __Secure-3PAPISID=K3LcRk50PtPrQJaS/AdNLhnvkACGmx_Q6v; __Secure-1PAPISID=K3LcRk50PtPrQJaS/AdNLhnvkACGmx_Q6v; SEARCH_SAMESITE=CgQIyZMB; OGPC=19022622-1:19025836-2:; SID=EQhWHdY7QbCUBA-1MSjkQhgkKBgDHEuI37-8qCYPyaEMacbDD0tAMrQrbAJ5pjtz7yD0hA.; __Secure-1PSID=EQhWHdY7QbCUBA-1MSjkQhgkKBgDHEuI37-8qCYPyaEMacbD4YORVLhE2tsO64TRYzCuOw.; __Secure-3PSID=EQhWHdY7QbCUBA-1MSjkQhgkKBgDHEuI37-8qCYPyaEMacbDFMDL73GMXdSUsthifcV9Kw.; NID=511=Xr_0WcTdAr2gR8niltUPt0vcOsGG53hHqD_wPID2Z-q3kmJ8ol4Ez6XvoCfKTxD5dozccDsexcS55v2Ki0m8-n_fns1q9tOlQvg1EjExBseocXLkmEIBn5JGKZrgLQeDYRQR9EWLXfnUSuNMo4OVhnsU-pvxYeE9cCJu5BHqELB9kRIgxaphS5BAD4DN60yWV5q5YYIA_4P7tzS5Sv8kePlxOpF6i3-9BmJ-VdVI3ZkOkHp2xLPeebErX-vS9IisPUYk42syjXMdPR9UGwi1w7JwzVaxgMiSx61AZwG2sLjKmg; SIDCC=AJi4QfHi6kIMl8Gmm9I-lvaNzcZZrsDadRNvFtd8Pxb75ylYYvGJvB8PNmvqxVe7p1zgIQ321w; __Secure-3PSIDCC=AJi4QfFV-xrZKp1EH_wdhNEf1t7OflugUYkiaQlx1HiYV152s9X_wo-xrwkP5aTzttsq0uoU2A'


HEADER = {
    'Host': 'docs.google.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://docs.google.com',
    'Referer': REFERER,
    'Cookie': COOKIE,
    'Upgrade-Insecure-Requests':'1'
    }

# After 4.8K+ requests google will ask you to fill a captcha if you are not using proxy.
PROXYS = []
# PROXYS = ['144.217.101.242:3129', '192.41.71.204:3128', '192.41.13.71:3128', '104.154.143.77:3128']




def trouble():
    try:
        if len(PROXYS) > 0: # Proxies are passed
            proxy = PROXYS[random.choice([x for x in range(len(PROXYS))])]
            r = requests.post(URL, proxies={'http':proxy, 'https':proxy}, data=DATA, headers=HEADER)
        else:
            r = requests.post(URL, data=DATA, headers=HEADER)
        return r
    except Exception as e:
        raise Exception (e)


if __name__ == "__main__":

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_calls = {executor.submit(trouble): count for count in range(SPAM_COUNT)}

        for future in as_completed(future_calls):
            try:
                result = future.result()
                print('[-] {}'.format(result.status_code))
            except Exception as e:
                print('[!] {}'.format(e))