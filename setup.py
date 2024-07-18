from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT = "-e ."
def get_requirements(filepath:str)->List[str]:
    """This Function will return List of Requirements"""
    requirements=[]
    with open(filepath) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements] # here remove new line char as Readlines return.
        
        # Here we are removing -e. from reqruirements.txt as -e . required to run setup.py but no need to install.
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
            
    
    
setup(
    name="ML_PROJECT",
    version="0.0.1",
    author="Vikas",
    author_email="vikas15122003@gmail.com",
    packages=find_packages(),
    include_dirs=get_requirements('requirements.txt')
    
)