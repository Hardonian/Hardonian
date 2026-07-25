import urllib.request
import json
import os

req = urllib.request.Request(f"https://api.github.com/repos/Hardonian/Hardonian/pulls/42/reviews", headers={"Authorization": f"Bearer {os.environ.get('GITHUB_TOKEN')}", "Accept": "application/vnd.github.v3+json"})
try:
    with urllib.request.urlopen(req) as response:
        print(response.read().decode())
except Exception as e:
    print(f"Error fetching PR comments: {e}")
