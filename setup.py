from setuptools import setup

setup(
    name="yay-faster-cn",
    version="0.11",
    py_modules=["yay_faster_cn"],
    entry_points={
        "console_scripts": [
            "yay-faster-cn = yay_faster_cn:main",
        ]
    },
    author="Haoze Zhang",
    license="MIT",
)