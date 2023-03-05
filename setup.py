from setuptools import find_packages, setup
from typing import List

Hyphen_e_Dot ='-e .'

def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace('\n', '') for req in requirements]

        if Hyphen_e_Dot in requirements:
            requirements.remove(Hyphen_e_Dot)


setup(
    name='mlproject',
    version='0.0.1',
    author='Shubham',
    author_email='shubham_khera@hotmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)