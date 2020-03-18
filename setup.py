from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="pyllama",
    version="0.0.4",
    author="Yi Zhen",
    author_email="zhenyi@gmail.com",
    description="A package to machine learning algorithms",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/camel4all/pyllama",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
