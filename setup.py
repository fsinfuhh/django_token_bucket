import os
import codecs
from setuptools import setup, find_packages


version = '0.2.3'


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


install_requires = [
    'Django>=1.11',
]


test_requires = [
]


setup(
    name='django_token_bucket',
    version=version,
    description='Django Tocken Bucket support.',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    author='Nils Rokita, Henning Pridöhl',
    author_email='0rokita@informatik.uni-hamburg.de',
    maintainer='Nils Rokita',
    maintainer_email='0rokita@informatik.uni-hamburg.de',
    url='https://github.com/fsinfuhh/django_token_bucket',
    license='License :: OSI Approved :: MIT License',
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
        'Framework :: Django',
    ]
)
