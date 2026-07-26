from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    """This function will return the list of requirements"""
    requirements = []
    with open(file_path) as requirement_file:
        requirements = requirement_file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="mlproject",
    version="0.1.0",
    author="Raunak",
    author_email="r.kbatra2005@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
) 