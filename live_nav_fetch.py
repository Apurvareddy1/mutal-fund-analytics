import requests

scheme_codes = [119551, 120503, 118632, 119092, 120841]

for code in scheme_codes:
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:
        print(f"Data fetched successfully for {code}")
    else:
        print(f"Failed for {code}")
        