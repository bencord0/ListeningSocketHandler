import os
from setuptools import setup
from pkg_resources import parse_requirements

req_fn = os.path.join(os.path.dirname(__file__), 'requirements.txt')
with open(req_fn) as f:
    requirements = f.read()

setup(
    name='ListeningSocketHandler',
    version='0.0.2',
    author='Ben Cordero',
    author_email='bmc@linux.com',
    packages=['ListeningSocketHandler', 'ListeningSocketHandler.test'],
    scripts=['bin/log-spewer.py', 'bin/log-reader.py'],
    url='https://github.com/bencord0/ListeningSocketHandler',
    license='LICENSE.txt',
    description='The opposite of logging.handlers.SocketHandler',
    long_description=open('README.txt').read(),
    install_requires=parse_requirements(requirements),
)
