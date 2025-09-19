import requests
from datetime import datetime

def prazniki_na_delovnikih(leto):

    url = f"https://date.nager.at/api/v3/PublicHolidays/{leto}/AT"
    podatki = requests.get(url).json()

    stevec = 0
    for praznik in podatki:
        datum = datetime.strptime(praznik['date'], "%Y-%m-%d")
        if datum.weekday() < 5:
            stevec += 1
    return stevec

if __name__ == "__main__":
    leto = 2026
    print(f"Število praznikov med tednom v {leto}: {prazniki_na_delovnikih(leto)}")