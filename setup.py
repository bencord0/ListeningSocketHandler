import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

from pkg_resources import parse_requirements

req_fn = os.path.join(os.path.dirname(__file__), 'requirements.txt')
with open(req_fn) as f:
    requires = parse_requirements(f.read())

class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)

setup(
    name='ListeningSocketHandler',
    version='0.0.2',
    author='Ben Cordero',
    author_email='bmc@linux.com',
    packages=['ListeningSocketHandler', 'tests'],
    url='https://github.com/bencord0/ListeningSocketHandler',
    license='LICENSE.txt',
    description='The opposite of logging.handlers.SocketHandler',
    long_description=open('README.txt').read(),
    install_requires=requires,
    tests_require=['tox'],
    cmdclass = {'test': Tox},
)
