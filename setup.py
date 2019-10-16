import os
import re

from setuptools import find_packages, setup


BASE_DIR = os.path.realpath(os.path.dirname(__file__))

def read(*parts):
    with open(os.path.join(BASE_DIR, *parts), 'r', encoding='utf-8') as f:
        return f.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r'^__version__ = ["\']([^"\']*)["\']', version_file, re.M)

    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name='dj_registry',
    version=find_version('registry', '__init__.py'),
    url='https://github.com/yychen/dj-registry',
    license='MIT',
    description='A simple, easy access key-value registry for Django.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='Tom Chiung-ting Chen',
    author_email='ctchen@gmail.com',
    packages=find_packages(exclude=['tests*']),
    python_requires=">=3",
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
