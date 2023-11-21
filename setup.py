from setuptools import find_packages,setup
from typing import List
import os

def get_requirements(file_path):
    """
    This Function will return the list of all required libraries.
    """
    #Write code to read requirements.txt file and append each requirement in requirement list variable

    requirement_list=[]
    with open(file_path, 'r') as file:
        for line in file:
            # Remove newline characters and any extra spaces
            item = line.strip()
            # Append the item to the list
            requirement_list.append(item)
    return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="MaheshJadhav",
    author_email="maheshjadhav7979@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt') #[]
)