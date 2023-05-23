import os
import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
import time

checked = 0
wallets_to_check = 10  # Number of wallets to check on each iteration

while True:
    os.system(f"title Bye Bye Bitcoin // Checked Wallets: {checked} // by clout")
    url = "https://www.bitcoinlist.io/random"
    headers = CaseInsensitiveDict()
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"

    try:
        req = requests.get(url, headers=headers)
        req.raise_for_status()  # Check for any HTTP request errors
        soup = BeautifulSoup(req.content, 'html.parser')
        wallets = soup.find_all("tr")[:wallets_to_check]  # Limit the number of wallets to check

        for wallet in wallets:
            checked += 1
            getwallet = wallet.get_text().strip().split()
            if len(getwallet) >= 4:
                privkey = getwallet[0]
                uncompaddy = getwallet[1]
                compaddy = getwallet[2]
                balance = getwallet[3]
                if float(balance) > 0:
                    with open('hits.txt', 'a+') as f:
                        f.write(f"{balance} BTC found in Address: {compaddy} // Private Key: {privkey}\n")

                os.system("cls")
                os.system(f"title Bye Bye Bitcoin // Checked Wallets: {checked} // by clout")
                print(f"""Private Key: {privkey}Uncompressed Address: {uncompaddy}Compressed Address: {compaddy}Balance: {balance}""")

        if checked >= wallets_to_check:
            break  # Stop iterating if the desired number of wallets have been checked

    except requests.exceptions.RequestException as e:
        print("An error occurred during the request:", e)

    time.sleep(0.001)
