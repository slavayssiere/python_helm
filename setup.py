import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='helm_python',  
    version='0.1.2',
    scripts=['helm_python'] ,
    author="Sebastien Lavayssiere",
    author_email="sebastien.lavayssiere@gmail.com",
    description="A Helm automation package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/slavayssiere/helm_python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )