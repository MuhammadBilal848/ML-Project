from setuptools import find_packages,setup
from typing import List


trigger = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''This function will return the list of requirements'''

    requirements = []
    with open('requirements.txt') as f:
        requirements = f.readlines()
        requirements = [ req.replace('\n','') for req in requirements ]

    if trigger in requirements:
        requirements.remove(trigger)
    
    return requirements


setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Bilal',
    author_email ='Bilalhanif848@gmail.com',
    packages = find_packages(),
    # when find_packages runs, it will find in every folder the '__init__.py' file,
    # in our case we have __init__ in src, so it will consider the src as package it 
    # will build __init__. 
    install_requires = get_requirements('requirements.txt'),
    # ['pandas','numpy','seaborn'] we cant write like this if we have 100s of requirements,
    # thats why we made function get_requirements
    
    



)
