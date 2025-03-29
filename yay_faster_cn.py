import clone
import parse
import download
import os
from pathlib import Path
import sys
def main():
    if len(sys.argv) < 2:
        print("Args too few.")
        return
    package = sys.argv[1]
    cache_dir = Path.home() / '.cache' / 'yay' / package
    print("Cloning from AUR...")
    clone.clone_repo(package, cache_dir)
    print("Getting sources...")
    sources = parse.get_sources(cache_dir)
    print("Source(s): ", sources)
    print("Downloading from source(s)...")
    download.download_from_sources(sources, cache_dir)
    print(f"Running `yay -S {package}`")
    print("!!! Enter `N` twice !!!")
    os.system(f"yay -S {package}")
if __name__ == '__main__':
    main()