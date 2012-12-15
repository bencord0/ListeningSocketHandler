import os
import sys

try:
    from setuptools import setup
except ImportErrror:
    from distutils.core import setup

req_fn = os.path.join(os.path.dirname(__file__), 'requirements.txt')
with open(req_fn) as f:
    requires = f.read().split()

setup(
    name='ListeningSocketHandler',
    version='0.0.2',
    author='Ben Cordero',
    author_email='bmc@linux.com',
    packages=['ListeningSocketHandler', 'tests'],
    url='https://github.com/bencord0/ListeningSocketHandler',
    license='LICENSE.txt',
    description='The opposite of logging.handlers.SocketHandler',
    long_description=open('README').read(),
    install_requires=requires,
    test_suite="tests.get_tests",
)
