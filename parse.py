import subprocess
import os

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
            if source[1].startswith('https://github.com/'):
                source[1] = 'https://ghfast.top/' + source[1]
            sources.append(source)

    return sources

