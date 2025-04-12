import subprocess
import os
import re

mirrors_table = {
    r"(https://github.com/.+)": "https://ghfast.top/{}",
    r"(https://raw.githubusercontent.com/.+)": "https://ghfast.top/{}",
    r"https://cdn.kernel.org/pub/linux/kernel/(.+)": "https://mirrors.tuna.tsinghua.edu.cn/kernel/{}"
}
def get_arch():
    arch = subprocess.getoutput("uname -m").lower()
    alias_map = {
        "x86_64": "x86_64",
        "aarch64": "aarch64",
        "armv8l": "aarch64", 
        "loongarch64": "loong64",
        "mips64": "mips64",
    }
    if not arch in alias_map:
        return arch
    return alias_map.get(arch, arch)

def get_sources(pkgbuild_dir):
    if not pkgbuild_dir.exists():
        print(f"Something went wrong. {pkgbuild_dir} doesn't exist.")
        return []
    arch_name = get_arch()
    result = subprocess.run(
        ['makepkg', '--printsrcinfo'],
        cwd=pkgbuild_dir,
        capture_output=True,
        text=True
    )
    sources = []
    for line in result.stdout.split('\n'):
        line = line.strip()
        if line.startswith('source = ') or line.startswith(f'source_{arch_name} = '):
            source_str = line.split(' = ', 1)[1].strip() # has ::
            if '::' in source_str:
                source = source_str.split('::') # 0: new name; 1: url
            else:
                source = []
                source.append('')
                source.append(source_str)
            for mirrorable in mirrors_table:
                matchObj = re.match(mirrorable, source[1])
                if matchObj:
                    source[1] = mirrors_table[mirrorable].format(matchObj.group(1))
                    break
            sources.append(source)

    return sources

