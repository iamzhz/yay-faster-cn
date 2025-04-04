import os
from urllib.parse import urlparse, unquote

def extract_filename(url: str) -> str:
    decoded_path = unquote(urlparse(url).path)
    path_parts = [p for p in decoded_path.split('/') if p]

    return path_parts[-1] if path_parts else ''

def is_get_from_internet(url):
    network_protocol = ["http", "https", "ftp"]
    startwith = url.split("://")[0]
    if startwith in network_protocol:
        return True
    return False

def download_from_sources(sources, cache_dir):
    for source in sources:
        if not is_get_from_internet(source[1]):
            continue
        print("Downloading from", source[1], "...")
        save_as = str(cache_dir)
        if source[0] == '':
            save_as += '/' + extract_filename(source[1])
        else:
            save_as += '/' + source[0]
        command = f"wget {source[1]} -O {save_as}"
        print(command)
        os.system(command)