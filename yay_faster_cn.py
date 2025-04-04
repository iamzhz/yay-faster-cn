import clone
import parse
import download
import utils
import os
from pathlib import Path
import sys
def main():
    # prepare
    if len(sys.argv) < 2:
        print("Args too few.")
        return
    package = sys.argv[1]
    cache_dir = Path.home() / '.cache' / 'yay' / package
    git_url = f'https://aur.archlinux.org/{package}.git'
    # check
    if not utils.is_package_in_aur(package):
        print(f"Cannot find `{package}` in AUR.")
        return 
    if cache_dir.exists():
        answer = input(f"The directory `{cache_dir}` has existed. Do you want to delete it? (y/N):")
        if answer.upper() == 'Y':
            utils.delete_the_whole_directory(cache_dir)
        else:
            print("Exit.")
            return
    # work
    print("Cloning from AUR...")
    if clone.clone_repo(git_url, cache_dir) == False:
        print(f"Something went wrong. Cannot clone from `{git_url}`")
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