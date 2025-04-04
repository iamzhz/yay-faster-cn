import subprocess
from urllib import request, error
from urllib.parse import urlencode
import json

def delete_the_whole_directory(dir):
    if not dir.exists():
        return
    if str(dir) == '/':  # just in case
        return
    subprocess.run(['rm', '-rf', str(dir)], check=False)

def is_package_in_aur(package: str) -> bool:
    params = urlencode({
        "v": 5,
        "type": "info",
        "arg": package
    })
    url = f"https://aur.archlinux.org/rpc/?{params}"
    
    try:
        with request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())
            return data.get("resultcount", 0) > 0
    except (error.URLError, error.HTTPError, json.JSONDecodeError):
        return False
    except Exception:
        return False