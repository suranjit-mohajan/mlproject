from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements from the given file.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]
        
        # Remove '-e .' if it's in the requirements
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Suranjit',
    author_email='suranjitmohajan@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")  # Install dependencies
)
