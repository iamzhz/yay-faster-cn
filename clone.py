import subprocess


def clone_repo(package: str, cache_dir: str):
    try:
        # generate url
        url = f'https://aur.archlinux.org/{package}.git'

        # generate target dir


        # run - git clone
        result = subprocess.run(
            ['git', 'clone', url, str(cache_dir)],
            capture_output=True,
            text=True
        )

        is_success = (
            result.returncode == 0
            and cache_dir.exists()
            and (cache_dir / '.git').exists()
        )
        
        if not is_success and cache_dir.exists():
            if str(cache_dir) == '/':
                return   # Just in case
            subprocess.run(['rm', '-rf', str(cache_dir)], check=False)
    
        return is_success
    except Exception:
        return False

