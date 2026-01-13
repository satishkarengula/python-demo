import time
import requests

with open("/Users/satish/python-demo/github_users.txt", "r") as file:
    for user in file:
        user = user.strip()  # remove newline
        page = 1
        while True:
            url = f"https://api.github.com/users/{user}/repos?per_page=100&page={page}"
            response = requests.get(url)
            
            if response.status_code != 200:
                print(f"Error fetching repos for {user}: {response.status_code}")
                break

            data = response.json()
            if not data:  # empty list means no more pages
                break

            for repo in data:
                if isinstance(repo, dict):
                    print(repo.get("name"))

            page += 1
            time.sleep(0.1)