from setuptools import find_packages,setup
from typing import List

hyphenedot = "-e ."
def get_requirements(file_path:str) -> List[str]:
    requirements = []
    
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]

    if hyphenedot in requirements:
        requirements.remove(hyphenedot)

    return requirements


setup(
name='MLProject',
version='0.0.1',
author='ansh',
author_email='agnihotriansh542@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)