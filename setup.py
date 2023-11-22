from setuptools import find_packages,setup
from typing import List
import os

#Declaring variables for setup functions
PROJECT_NAME="sensor"
VERSION="0.0.1"
AUTHOR="Mahesh Jadhav"
AUTHOR_EMAIL="maheshjadhav7979@gmail.com"

REQUIREMENT_FILE_NAME="requirements.txt"

HYPHEN_E_DOT = "-e ."


def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list
# def get_requirements(file_path):
#     """
#     This Function will return the list of all required libraries.
#     """
#     #Write code to read requirements.txt file and append each requirement in requirement list variable

#     requirement_list=[]
#     with open(file_path, 'r') as file:
#         for line in file:
#             # Remove newline characters and any extra spaces
#             item = line.strip()
#             # Append the item to the list
#             requirement_list.append(item)
#     return requirement_list

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages= find_packages(),
    install_requires= get_requirements_list() #[]
)