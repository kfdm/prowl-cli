from setuptools import setup

setup(
    name='prowl',
    description='Prowl CLI',
    author='Paul Traylor',
    url='https://github.com/kfdm/prowl-cli',
    version='0.0.1',
    packages=[
        'prowl',
    ],
    install_requires=[
        'pushnotify',
    ],
    entry_points={
        'console_scripts': [
            'prowl = prowl:main'
        ]
    }
)
