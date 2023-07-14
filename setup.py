from setuptools import setup, find_packages
from thesisperu.version import version

setup(
    name='thesisperu',
    version=version,
    description='Descarga la metada de las tesis',
    url='hhttps://github.com/TJhon/tesis_peru',
    author='Jhon',
    author_email='fr.jhonk@gmail.com',
    packages=find_packages(),
)
