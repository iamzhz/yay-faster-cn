import subprocess
import utils

def clone_repo(url: str, cache_dir):
    try:
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
        
        if not is_success:
            utils.delete_the_whole_directory(cache_dir)
    
        return is_success
    except Exception:
        return False

