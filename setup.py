from setuptools import setup, find_packages


setup(
    name='cli_package',
    version='0.0.5',
    packages=['cli_package'],
    url='URL',
    license='License',
    author='Andy Phillips',
    author_email='phillipsaje@gmail.com',
    description='My Practice CLI',
    entry_points={
        'console_scripts': [
            'hello=cli_package.__main__:main'
        ]
    })
