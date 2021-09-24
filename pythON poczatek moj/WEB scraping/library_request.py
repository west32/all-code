import requests

def run_example():
    try:
        response = requests.get("http://infoshareacademy.com?")
    except requests.RequestException as error:
        print(f"Błąd przy połączeniu {error}")
        return
    try:
        response.raise_for_status()
    except requests.HTTPError as error:
        print(f'Żądanie zakończone niepowodzeniem {error}')
        return

    print(response.text)


if __name__ =="__main__":
    run_example()