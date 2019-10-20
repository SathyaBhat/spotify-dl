#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = '3.3.0'

setup(
    name='spotify_dl',
    version=version,
    python_requires='>=3',
    install_requires=requirements,
    author='Sathya Bhat',
    author_email='sathya@sathyasays.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/SathyaBhat/spotify-dl/',
    license='MIT',
    description='Downloads songs from a '
                'Spotify Playlist that you provide',
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
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
