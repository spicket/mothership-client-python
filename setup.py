from distutils.core import setup

setup(
    name='mothership-client',
    version='1.0.0',
    packages=['mothership',],
    license='MIT',
    long_description=open('README.txt').read(),
    url='https://github.com/spicket/mothership-client-python',
    install_requires=[
        'requests'
    ]
)