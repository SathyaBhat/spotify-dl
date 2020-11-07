#!/usr/bin/env python

from setuptools import setup, find_packages
from spotify_dl.constants import VERSION

with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='spotify_dl',
    version=VERSION,
    python_requires='>=3.6',
    install_requires=requirements,
    author='Sathya Bhat',
    author_email='sathya@sathyasays.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/SathyaBhat/spotify-dl/',
    license='MIT',
    description='Downloads songs from a Spotify Playlist/Track/Album that you provide',
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'spotify_dl=spotify_dl.spotify_dl:spotify_dl',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
