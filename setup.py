import io
from pathlib import Path

from discogs_cli.__init__ import __version__


from setuptools import setup, find_packages


description = 'View and search for artists, labels and releases in the Discogs.com library, from the command line.'
try:
    with io.open('README.rst', encoding="utf-8") as fh:
            long_description = fh.read()
except IOError:
    long_description = description


setup(
    name='discogs-cli',
    description=description,
    long_description=long_description,
    author='Jesse Ward',
    author_email='jesse@jesseward.com',
    version=__version__,
    url='https://github.com/jesseward/discogs-cli',
    license='MIT',
    install_requires=Path('requirements.txt').read_text().splitlines(),
    entry_points={
        'console_scripts': [
            'discogs-cli = discogs_cli.main:cli',
            'ogs = discogs_cli.main_cli:cli',
        ]
    },
    packages=find_packages(),
    scripts=[],
    classifiers=[
        'Environment :: Console',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
