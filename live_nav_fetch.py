import requests
import pandas as pd

scheme_codes = [119551, 120503, 118632, 119092, 120841]

for code in scheme_codes:
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        nav_df.to_csv(f"data/raw/nav_{code}.csv", index=False)

        print(f"Saved nav_{code}.csv")

    else:
        print(f"Failed for {code}")