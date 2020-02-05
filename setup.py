from setuptools import setup, find_packages

setup(
    name='trytopackage', #the name package managers will use for your project, like numpy or pandas
    version='0.1', #the current version number of your project
    packages=find_packages(exclude=['tests*']),
    license='MIT', #name of the license you chose
    description='EDSA example python package', #one-sentence description of your package
    long_description=open('README.md').read(),
    install_requires=['numpy'], #list of all other packages this package depends on; package managers will install these automatically as needed
    url='https://github.com/OmphileL/trytopack.git',
    author='Omphile Louw',
    author_email='12779027+OmphileL@users.noreply.github.com'
)
