import os
from setuptools import setup, find_packages

__version__ = ""
packages = find_packages(exclude=["tests*"])

fn = os.path.join("simdak", "version.py")
with open(fn) as fh:
    code = compile(fh.read(), fn, "exec")
    exec(code)


setup(
    name="simdak",
    version=__version__,
    author="hexatester",
    license="GPLv3",
    url="https://github.com/dapodix/simdak",
    keywords="dapodik simdak paud-dikmas kemdikbud",
    description="Importer-exporter data Simdak Kemdikbud",
    packages=packages,
    package_data={"simdak": ["template/*.xlsx"]},
    install_requires=["python", "requests", "bs4", "openpyxl", "click"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Education :: Testing",
        "Topic :: Education",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={"console_scripts": ["simdak=simdak.__main__:main"]},
)
