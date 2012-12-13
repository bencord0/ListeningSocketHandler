from distutils.core import setup

setup(
    name='ListeningSocketHandler',
    version='0.0.1',
    author='Ben Cordero',
    author_email='bmc@linux.com',
    packages=['listeningsockethandler'],
    url='https://github.com/bencord0/ListeningSocketHandler',
    license='LICENSE.txt',
    description='The opposite of logging.handlers.SocketHandler',
    long_description=open('README.txt').read(),
)
